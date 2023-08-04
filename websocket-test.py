#test websocket service in python
import websocket
def on_message(ws, message):
    print("Received: " + message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("### open ###")
    ws.send("Hello World")

if __name__ == "__main__":
    websocket.enableTrace(True)
    # ws = websocket.WebSocketApp("ws://10.0.2.6:16017",
    
    # ws = websocket.WebSocketApp("ws://180.169.157.165:16011",
    ws = websocket.WebSocketApp("ws://127.0.0.1:8765",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()        