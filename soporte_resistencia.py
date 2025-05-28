def calcular_niveles(df):
    soporte = df['low'].rolling(window=10).min().iloc[-1]
    resistencia = df['high'].rolling(window=10).max().iloc[-1]
    return soporte, resistencia
