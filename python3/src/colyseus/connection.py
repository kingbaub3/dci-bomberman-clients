import msgpack
from colyseus.webSocketClient import WebSocketClient

# Wraps the socket client into its own thread
class Connection:
    def __init__(self, url, on_open=None, on_message=None, on_error=None, on_close=None):
        self.ws = WebSocketClient(url, on_open, on_message, on_error, on_close)

    def send(self, message):
        encodedMessage = msgpack.packb(message)
        self.ws.send(encodedMessage)
        print("Message: ", message, "sent!")

    def run_forever(self):
        self.ws.run_forever()