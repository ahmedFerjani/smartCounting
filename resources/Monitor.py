from flask_restful import Resource
from flask import request
from datetime import datetime

from database.models import Monitor
from database.schema import monitor_schema, monitors_schema
from app import db


class MonitorApi(Resource):
    def get(self):
        all_monitors = db.session.query(Monitor).all()
        result = monitors_schema.dump(all_monitors)
        return monitors_schema.jsonify(result)

    def post(self):
        new_monitor = Monitor(start_date=datetime.now())
        db.session.add(new_monitor)
        db.session.commit()
        return monitor_schema.dump(new_monitor)


class MonitorDetailsApi(Resource):
    def get(self, id):
        fetched_monitor = db.session.query(Monitor).get(id)
        return monitor_schema.dump(fetched_monitor), 200

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


class MonitorStop(Resource):
    def post(self, id):
        fetched_monitor = db.session.query(Monitor).get(id)
        fetched_monitor.end_date = datetime.now()
        db.session.commit()
        return monitor_schema.dump(fetched_monitor)