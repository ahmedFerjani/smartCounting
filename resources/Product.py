from flask_restful import Resource
from flask import request
from datetime import datetime

from database.models import Product
from database.schema import product_schema, products_schema
from app import db


class ProductApi(Resource):
    def get(self):
        all_products = db.session.query(Product).all()
        result = products_schema.dump(all_products)
        return products_schema.jsonify(result)

    def post(self):
        name = request.json['name']
        company = request.json['company']
        #production_date = request.json['production_date']
        #expiration_date = request.json['expiration_date']
        description = request.json['description']
        qrcode = request.json['qrcode']

        new_product = Product(name,company, description,qrcode)
        db.session.add(new_product)
        db.session.commit()
        return product_schema.dump(new_product)


class ProductDetailsApi(Resource):
    def get(self, id):
        fetched_product = db.session.query(Product).get(id)
        return product_schema.dump(fetched_product), 200

    def put(self, id):
        fetched_product = db.session.query(Product).get(id)
        fetched_product.name = request.json['name']
        fetched_product.company = request.json['company']
        fetched_product.production_date = request.json['production_date']
        fetched_product.expiration_date = request.json['expiration_date']
        fetched_product.description = request.json['description']
        fetched_product.qrcode = request.json['qrcode']
        db.session.commit()
        return product_schema.dump(fetched_product)

    def delete(self,id):
        fetched_product = db.session.query(Product).get(id)
        db.session.commit()
        return product_schema.dump(fetched_product), 200
