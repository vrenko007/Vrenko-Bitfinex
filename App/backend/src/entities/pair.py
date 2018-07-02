# coding=utf-8

from marshmallow import Schema, fields
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .entity import Entity, Base


class Pair(Entity, Base):
    __tablename__ = 'pairs'

    title = Column(String(128))
    channels = relationship("PairChannel")

    def __init__(self, title):
        Entity.__init__(self)
        self.title = title


class PairSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()