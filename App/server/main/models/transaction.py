# -*- coding: utf-8 -*-

from sqlalchemy import inspect

from server.main import db
from sqlalchemy.sql import func


class BaseModel(db.Model):
    """Base data model for all objects"""
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        """Define a base way to print models"""
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self.as_dict().items()
        })

    # def _as_dict(self):
    #     return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # Preferred way
    # https://stackoverflow.com/questions/1958219/convert-sqlalchemy-row-object-to-python-dict
    def as_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class Transaction(BaseModel, db.Model):
    """Model for transaction table"""
    __tablename__ = "transaction"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bitfinex_id = db.Column(db.Integer, nullable=False)
    bitfinex_currency = db.Column(db.String(128), nullable=False)
    bitfinex_timestamp = db.Column(db.Integer, nullable=False)
    bitfinex_price = db.Column(db.Float, nullable=False)
    bitfinex_amount = db.Column(db.Float, nullable=False)
    # using func.now(), so time is calculated by the DB server and not by app server.
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    created_date = db.Column(db.DateTime, nullable=False, default=func.now())

    def __init__(self, bitfinex_id, bitfinex_currency, bitfinex_timestamp,bitfinex_price,bitfinex_amount):
        super().__init__()
        self.bitfinex_id = bitfinex_id
        self.bitfinex_currency = bitfinex_currency
        self.bitfinex_timestamp = bitfinex_timestamp
        self.bitfinex_price = bitfinex_price
        self.bitfinex_amount = bitfinex_amount
