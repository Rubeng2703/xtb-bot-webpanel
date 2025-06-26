import time

from bot import TradingBot

if __name__ == "__main__":
    bot = TradingBot()
    while True:
        try:
            bot.ejecutar()
            print("⏳ Esperando 5 minutos para próxima evaluación...")
            time.sleep(300)  # Espera 5 minutos entre ejecuciones
        except Exception as e:
            print("🛑 Error detectado:", e)
            time.sleep(60)  # Espera 1 minuto si hubo error

