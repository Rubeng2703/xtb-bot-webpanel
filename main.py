import websocket
import json
from config import XTB_LOGIN, XTB_PASSWORD, XTB_HOST

class XTBApi:
    def __init__(self):
        self.ws = websocket.create_connection(f"wss://{XTB_HOST}/demo")

    def login(self):
        payload = {
            "command": "login",
            "arguments": {
                "userId": XTB_LOGIN,
                "password": XTB_PASSWORD
            }
        }
        self.ws.send(json.dumps(payload))
        response = self.ws.recv()
        return json.loads(response)

    def get_candles(self, symbol="EURUSD", timeframe="M5", count=100):
        payload = {
            "command": "getChartLastRequest",
            "arguments": {
                "info": {
                    "period": timeframe,
                    "start": 0,
                    "symbol": symbol
                }
            }
        }
        self.ws.send(json.dumps(payload))
        response = self.ws.recv()
        return json.loads(response)

