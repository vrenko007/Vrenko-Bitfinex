from socketIO_client import SocketIO


def on_connect():
    print('connect')

def on_disconnect():
    print('disconnect')

def on_reconnect():
    print('reconnect')

def on_response(*args):
    print(args[0])

socketIO = SocketIO('127.0.0.1', 5000, verify=False)
socketIO.on('connect', on_connect)
socketIO.on('disconnect', on_disconnect)
socketIO.on('reconnect', on_reconnect)
# Listen
socketIO.on('transaction', on_response)

socketIO.emit('join',{ "room":"BTCUSD" })

socketIO.wait(seconds=15)