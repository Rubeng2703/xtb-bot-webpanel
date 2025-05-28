import pandas as pd
from ta.momentum import RSIIndicator

def analizar_estrategia(df):
    # Calcular RSI
    rsi = RSIIndicator(close=df['close'], window=14)
    df['rsi'] = rsi.rsi()

    # Detectar patrón envolvente alcista
    df['envolvente'] = (
        (df['close'].shift(1) < df['open'].shift(1)) &
        (df['close'] > df['open']) &
        (df['close'] > df['open'].shift(1)) &
        (df['open'] < df['close'].shift(1))
    )

    # Señal de compra si RSI < 30 y patrón envolvente
    return df.iloc[-1]['rsi'] < 30 and df.iloc[-1]['envolvente']
