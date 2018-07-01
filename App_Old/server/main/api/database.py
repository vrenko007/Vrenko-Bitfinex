from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for

from data_provider_service import DataProviderService

db_engine = 'mysql+mysqldb://packtuser:secret@localhost/packtwebapi?unix_socket=/opt/lampp/var/mysql/mysql.sock'


DATA_PROVIDER = DataProviderService(db_engine)


def transaction(serialize = True):
    transactions = DATA_PROVIDER.get_transaction(serialize=serialize)
    if serialize:
        return jsonify({"transactions": transactions, "total": len(transactions)})
    else:
        return transactions


def transaction_by_id(id):
    current_transaction = DATA_PROVIDER.get_transaction(id, serialize=True)
    if current_transaction:
        return jsonify({"transaction": current_transaction})
    else:
        #
        # In case we did not find the transaction by id
        # we send HTTP 404 - Not Found error to the client
        #
        abort(404)


def initialize_database():
    DATA_PROVIDER.init_database()

def get_last_transactions(self, bitfinex_currency=None, nr_of_transactions=20, serialize=false):
    transactions = DATA_PROVIDER.get_last_transactions(bitfinex_currency,nr_of_transactions,serialize)
    return jsonify({"transactions": transactions, "total": len(transactions)})

def add_transaction(bitfinex_id, bitfinex_currency, bitfinex_timestamp, bitfinex_price, bitfinex_amount):
    new_transaction_id = DATA_PROVIDER.add_transaction(bitfinex_id, bitfinex_currency, bitfinex_timestamp, bitfinex_price, bitfinex_amount):

    return jsonify({
        "id": new_transaction_id,
        "url": url_for("transaction_by_id", id=new_transaction_id)
    })


def build_message(key, message):
    return {key:message}
