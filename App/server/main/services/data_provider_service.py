from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime

from main.models.transaction import Transaction

class DataProviderService:
    def __init__(self, engine):
        """
        :param engine: The engine route and login details
        :return: a new instance of DAL class
        :type engine: string
        """
        if not engine:
            raise ValueError('The values specified in engine parameter has to be supported by SQLAlchemy')
        self.engine = engine
        db_engine = create_engine(engine)
        db_session = sessionmaker(bind=db_engine)
        self.session = db_session()

    def init_database(self):
        """
        Initializes the database tables and relationships
        :return: None
        """
        init_database(self.engine)

        
    def init_database(engine):
        db_engine = create_engine(engine, echo=True)
        Transaction.metadata.create_all(db_engine)

    def add_transaction(self, bitfinex_id, bitfinex_currency, bitfinex_timestamp, bitfinex_price, bitfinex_amount):
        """
        Creates and saves a new transaction to the database.

        :param bitfinex_id: ID from bitfinex api
        :param bitfinex_currency: Currency from bitfinex api
        :param bitfinex_timestamp: Timestamp from bitfinex api
        :param bitfinex_price: Price from bitfinex api
        :param bitfinex_amount: Amount from bitfinex api
        :return: The id of the new transaction
        """

        new_transaction = Transaction(bitfinex_id=bitfinex_id,
                                  bitfinex_currency=bitfinex_currency,
                                  bitfinex_timestamp=bitfinex_timestamp,
                                  bitfinex_price=bitfinex_price,
                                  bitfinex_amount=bitfinex_amount,
                                  languages=languages,
                                  skills=skills)

        self.session.add(new_transaction)
        self.session.commit()

        return new_transaction.id

    def get_transaction(self, id=None, serialize=False):
        """
        If the id parameter is  defined then it looks up the transaction with the given id,
        otherwise it loads all the transactions

        :param id: The id of the transaction which needs to be loaded (default value is None)
        :return: The transaction or transactions.
        """

        all_transactions = []

        if id is None:
            all_transactions = self.session.query(transaction).order_by(transaction.bitfinex_currency).all()
        else:
            all_transactions = self.session.query(transaction).filter(transaction.id == id).all()

        if serialize:
            return [transact.serialize() for transact in all_transactions]
        else:
            return all_transactions

    def get_last_transactions(self, bitfinex_currency=None, nr_of_transactions=20, serialize=false):
        """
        If the id parameter is  defined then it looks up the transaction with the given id,
        otherwise it loads all the transactions

        :param id: The id of the transaction which needs to be loaded (default value is None)
        :return: The transaction or transactions.
        """

        all_transactions = []

        if id is None:
            all_transactions = self.session.query(transaction).order_by(transaction.created_date).limit(nr_of_transactions)
        else:
            all_transactions = self.session.query(transaction).filter(transaction.bitfinex_currency == bitfinex_currency).all()

        if serialize:
            return [transact.as_dict() for transact in all_transactions]
        else:
            return all_transactions