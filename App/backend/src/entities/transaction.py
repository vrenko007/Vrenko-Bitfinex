# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String, Integer, Float, ForeignKey

from .entity import Entity, Base


class Transaction(Entity, Base):
    __tablename__ = 'transactions'

    bitfinex_channel = Column(Integer, ForeignKey('pair_channels.id'))
    bitfinex_id = Column(Integer, nullable=False)
    bitfinex_currency = Column(String(128), nullable=False)
    bitfinex_timestamp = Column(Integer, nullable=False)
    bitfinex_price = Column(Float, nullable=False)
    bitfinex_amount = Column(Float, nullable=False)


    def __init__(self, bitfinex_channel, bitfinex_id, bitfinex_currency, bitfinex_timestamp, bitfinex_price, bitfinex_amount):
        Entity.__init__(self)
        self.bitfinex_channel = bitfinex_channel.id
        self.bitfinex_id = bitfinex_id
        self.bitfinex_currency = bitfinex_currency
        self.bitfinex_timestamp = bitfinex_timestamp
        self.bitfinex_price = bitfinex_price
        self.bitfinex_amount = bitfinex_amount

class TransactionSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    bitfinex_channel = fields.Number()
    bitfinex_id = fields.Number()
    bitfinex_currency = fields.Str()
    bitfinex_timestamp = fields.Number()
    bitfinex_price = fields.Number()
    bitfinex_amount = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()