from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db, ma


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    company = db.Column(db.String(100))
    qrcode = db.Column(db.String(100))
    #production_date = db.Column(db.Date)
    #expiration_date = db.Column(db.Date)
    description = db.Column(db.String(100))
    monitors = relationship('Monitor', secondary='monitor_product')

    def __init__(self, name, company, description, qrcode):
        self.name = name
        self.company = company
        #self.production_date = production_date
        #self.expiration_date = expiration_date
        self.description = description
        self.qrcode = qrcode

class Monitor(db.Model):
    __tablename__ = 'monitor'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    products = relationship('Product', secondary='monitor_product')


class MonitorProduct(db.Model):
    __tablename__ = 'monitor_product'
    __mapper_args__ = {
        'confirm_deleted_rows': 'False'
    }
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(Integer,ForeignKey('product.id',  onupdate="CASCADE", ondelete="CASCADE"))
    #product = db.relationship('Product', backref='monitor_product1', lazy="subquery")
    monitor_id = db.Column(Integer,ForeignKey('monitor.id', onupdate="CASCADE", ondelete="CASCADE"))
    #monitor = db.relationship('Monitor', backref='monitor_product2', lazy="subquery")
    number = Column(Integer)

    def __init__(self,product_id, monitor_id, number):
        self.product_id = product_id
        self.monitor_id = monitor_id
        self.number = number

