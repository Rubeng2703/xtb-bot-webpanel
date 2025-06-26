import time

from main import XTBApi
from estrategia import analizar_estrategia
from noticias import revisar_noticias
from soporte_resistencia import calcular_niveles
from ordenes import abrir_operacion
import time

class TradingBot:
    def __init__(self):
        self.api = XTBApi()

    def ejecutar(self):
        self.api.login()

        # Revisa si hay noticias importantes
        if revisar_noticias():
            print("⚠️ Hay noticias importantes. Se suspende la operación.")
            return

        # Obtiene datos del mercado
        data = self.api.get_candles(symbol="EURUSD", timeframe="M5", count=100)

        # Calcula niveles técnicos
        soporte, resistencia = calcular_niveles(data)
        print(f"Soporte: {soporte}, Resistencia: {resistencia}")

        # Evalúa si hay señal de compra
        if analizar_estrategia(data):
            print("✅ Señal detectada. Enviando orden.")
            abrir_operacion(self.api, symbol="EURUSD", lotes=0.1, sl=soporte, tp=resistencia)
        else:
            print("❌ No hay señal clara de entrada.")

        self.api.ws.close()
