# coding=utf-8

import eventlet

eventlet.monkey_patch()

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

db_url = '127.0.0.1:3306'
db_name = 'Vrenko-Bitfinex'
db_user = 'Vrenko-Bitfinex'
db_password = 'Super111Complicated222'
engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}')
Session = sessionmaker(bind=engine)

Base = declarative_base()

def make_session():
    return sessionmaker(bind=engine)


class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()