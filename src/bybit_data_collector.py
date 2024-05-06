import httpx
import pandas as pd
import asyncio

async def fetch_klines(symbol, interval, from_timestamp, limit=200):
    """
    Асинхронно получает исторические данные курсов для заданной криптовалютной пары с API Bybit.

    Параметры:
    symbol : str
        Символ пары, например 'BTCUSDT'.
    interval : str
        Интервал времени между данными, например '1' для 1 минуты, 'D' для одного дня.
    from_timestamp : int
        Начальная дата в формате UNIX timestamp.
    limit : int
        Количество возвращаемых свечей.

    Возвращает:
    pd.DataFrame
        DataFrame с данными о свечах.
    """

    url = 'https://api.bybit.com/v2/public/kline/list'
    params = {
        'symbol': symbol,
        'interval': interval,
        'from': from_timestamp,
        'limit': limit
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    
        if data['ret_code'] == 0:
            df = pd.DataFrame(data['result'])
            df['open_time'] = pd.to_datetime(df['open_time'], unit='s')
            return df
        else:
            raise Exception(f"API Error: {data['ret_msg']}")

async def main():
    data = await fetch_klines('BTCUSDT', '1', 1581234567)
    print(data.head())
    data.to_csv('historical_data_bybit.csv', index=False)

if __name__ == '__main__':
    asyncio.run(main())

