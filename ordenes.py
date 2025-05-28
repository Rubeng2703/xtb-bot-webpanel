import json
def abrir_operacion(api, symbol, lotes, sl, tp):
    orden = {
        "command": "tradeTransaction",
        "arguments": {
            "tradeTransInfo": {
                "cmd": 0,  # 0=Buy, 1=Sell
                "customComment": "BotAuto",
                "expiration": 0,
                "offset": 0,
                "order": 0,
                "price": 0.0,
                "sl": sl,
                "tp": tp,
                "symbol": symbol,
                "type": 0,
                "volume": lotes
            }
        }
    }
    api.ws.send(json.dumps(orden))
    return api.ws.recv()
