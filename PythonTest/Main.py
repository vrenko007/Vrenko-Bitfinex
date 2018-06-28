import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time

from json import JSONDecoder

id = 0

def on_message(ws, message):
    print(message)
    array = JSONDecoder().decode(message)
    if type(array) is dict:
        print(array["chanId"])
        id = array["chanId"]
        def run(*args):
            for i in range(10):
                time.sleep(1)
            ws.send('{"event":"unsubscribe","chanId":"'+str(args[0])+'"}')
            time.sleep(1)
            ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, (id))

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"event":"subscribe","channel":"trades","pair":"BTCUSD"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://api.bitfinex.com/ws",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()