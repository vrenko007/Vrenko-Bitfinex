# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class PairChannel(Entity, Base):
    __tablename__ = 'pair_channels'

    pair_id = Column(Integer, ForeignKey('pairs.id'))
    channel_number = Column(Integer)
    transactions = relationship("Transaction")

    def __init__(self, pair, channel_number):
        Entity.__init__(self)
        self.pair_id = pair.id
        self.channel_number = channel_number


class PairChannelSchema(Schema):
    id = fields.Number()
    pair_id = fields.Number()
    channel_number = fields.Number()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()