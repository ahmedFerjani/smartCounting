from flask_restful import Resource
from flask import request
from datetime import datetime

from database.models import *
from database.schema import *
from app import db


class MonitorProductApi(Resource):
    def get(self):
        jsonFinalResponse = list()
        monitors_products = db.session.query(MonitorProduct).all()
        print(monitors_products)
        for monitor_products in monitors_products:
            print("**2**")
            print(monitor_products.product_id)
            fetched_monitor = db.session.query(Monitor).filter(MonitorProduct.monitor_id==monitor_products.id).all()
            jsonResponse = {"monitor": monitor_schema.dump(fetched_monitor), "list": list()}
            print(jsonResponse)
            for monitor_product in monitor_products:
                responseObj = {"product": {}, "number": monitor_product.number}
                fetched_product = db.session.query(Product).get(monitor_product.product_id)
                responseObj["product"] = product_schema.dump(fetched_product)
                jsonResponse["list"].append(responseObj)
            jsonFinalResponse.append(jsonResponse)
        return jsonFinalResponse, 200

    def post(self):
        new_monitor = Monitor(start_date=datetime.now())
        db.session.add(new_monitor)
        db.session.commit()
        return monitor_schema.dump(new_monitor)


class MonitorProductDetailsApi(Resource):
    #get list of products for a specefic monitor
    def get(self, id):
        monitor_products = db.session.query(MonitorProduct).filter(MonitorProduct.monitor_id==id).all()
        fetched_monitor = db.session.query(Monitor).get(id)
        jsonResponse = {"monitor": monitor_schema.dump(fetched_monitor), "list": list()}
        for monitor_product in monitor_products:
            responseObj = {"product": {}, "number": monitor_product.number}
            fetched_product = db.session.query(Product).get(monitor_product.product_id)
            responseObj["product"] = product_schema.dump(fetched_product)
            jsonResponse["list"].append(responseObj)
        return jsonResponse, 200

    def put(self, id):
        fetched_monitor = db.session.query(Monitor).get(id)
        fetched_monitor.start_date = request.json['start_date']
        fetched_monitor.end_date = request.json['end_date']
        db.session.commit()
        return monitor_schema.dump(fetched_monitor)

    def delete(self,id):
        fetched_monitor = db.session.query(Monitor).get(id)
        db.session.commit()
        return monitor_schema.dump(fetched_monitor), 200