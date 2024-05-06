import pandas as pd
from pybit.unified_trading import HTTP

def fetch_klines(symbol: str, interval: int, start: int, end: int) -> pd.DataFrame:
    """
    Получает исторические данные курсов для заданной криптовалютной пары с Bybit.

    Параметры:
    symbol : str
        Символ пары, например 'BTCUSD'.
    interval : int
        Интервал времени между данными в минутах (например, 60 для 1 часа).
    start : int
        Начальная дата в миллисекундах UNIX timestamp.
    end : int
        Конечная дата в миллисекундах UNIX timestamp.

    Возвращает:
    pd.DataFrame
        DataFrame с данными о свечах.
    """
    session = HTTP(testnet=True)  # Измените на testnet=False для реальной торговли
    response = session.get_kline(
        category="inverse",
        symbol=symbol,
        interval=interval,
        start=start,
        end=end
    )

    # Обработка данных
    if response['retCode'] == 0:
        # Создание DataFrame из списка котировок
        columns = ['open_time', 'open_price', 'high_price', 'low_price', 'close_price', 'volume', 'turnover']
        df = pd.DataFrame(response['result']['list'], columns=columns)
        # Конвертация времени из миллисекунд в нормальную дату/время
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        # Конвертация строк в числа, где это необходимо
        df[['open_price', 'high_price', 'low_price', 'close_price', 'volume', 'turnover']] = df[['open_price', 'high_price', 'low_price', 'close_price', 'volume', 'turnover']].apply(pd.to_numeric)
        return df
    else:
        raise Exception(f"API Error: {response['retMsg']}")

if __name__ == "__main__":
    data = fetch_klines('BTCUSD', 60, 1670601600000, 1670608800000)
    print(data.head())


