# coding=utf-8

from flask import Flask, jsonify, request

from .entities.entity import Session, engine, Base
from .entities.pair import Pair, PairSchema
from .entities.pair_channel import PairChannel, PairChannelSchema
from .entities.transaction import Transaction, TransactionSchema
from flask_socketio import SocketIO, send, emit
from flask_socketio import join_room, leave_room
from sqlalchemy import func
import websocket
from json import JSONDecoder, JSONEncoder

import eventlet

eventlet.monkey_patch()

# creating the Flask application
app = Flask(__name__)
socketio = SocketIO(app)

# if needed, generate database schema
Base.metadata.create_all(engine)

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    transactions = get_last_20_transactions(room)
    schema = TransactionSchema()
    for transaction in transactions:
        emit("transaction", schema.dump(transaction))


@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)



rooms = {
}
def create_pair(array):
    session = Session()
    scalar = session.query(Pair).filter(Pair.title.like(array["pair"])).count()
    if(scalar < 1):
        tmpPair = Pair(array["pair"])
        session.add(tmpPair)
        session.commit()
    pair = session.query(Pair).filter(Pair.title.like(array["pair"])).first()
    tmpPairChannel = PairChannel(pair, array["chanId"])
    session.add(tmpPairChannel)
    session.commit()
    session.close()


def create_transaction(array):
    session = Session()
    #[3,"tu","1338212-BTCUSD",264088478,1530487575,6383.5,-0.005]
    stack = session.query(Pair, PairChannel).filter(Pair.id == PairChannel.pair_id).filter(Pair.title == rooms[array[0]], PairChannel.channel_number==array[0]).order_by(PairChannel.created_at.desc()).first()
    channel = stack[1]
    session.add(Transaction(channel, array[3], array[2], array[4], array[5], array[6]))
    session.commit()
    session.close()

def get_last_20_transactions(group):
    session = Session()
    stack = session.query(Transaction).join(PairChannel).join(Pair).filter(Pair.title == group).order_by(Transaction.created_at.desc())[0:20]
    session.close()
    return stack[::-1]


def on_message(ws, message):
    array = JSONDecoder().decode(message)
    if type(array) is dict:
        create_pair(array)
        rooms[array["chanId"]] = array["pair"]
    elif((array[0] in rooms) and (array[1] == "te")):
        socketio.emit('transaction', message, room=rooms[array[0]])
    elif((array[0] in rooms) and (array[1] == "tu")):
        print(message)
        create_transaction(array)




def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"event":"subscribe","channel":"trades","pair":"ETHUSD"}')
    ws.send('{"event":"subscribe","channel":"trades","pair":"BTCUSD"}')
    ws.send('{"event":"subscribe","channel":"trades","pair":"XRPUSD"}')
    print(ws)

#BitFinex API
def run_job():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

eventlet.spawn(run_job)

if __name__ == '__main__':

    socketio.run(app)