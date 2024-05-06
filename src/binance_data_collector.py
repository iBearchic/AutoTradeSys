from binance.client import Client
import pandas as pd
from config.secrets import load_secrets

def fetch_data() -> pd.DataFrame:
    # Загрузка API ключей
    api_key, api_secret = load_secrets()
    client = Client(api_key, api_secret)

    try:
        candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Jan, 2023", "1 Jan, 2024")
        columns = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']
        df = pd.DataFrame(candles, columns=columns)
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
        df[['open', 'high', 'low', 'close', 'volume']] = df[['open', 'high', 'low', 'close', 'volume']].apply(pd.to_numeric)
        return df
    except Exception as e:
        print(f"Ошибка: {e}")
        raise


if __name__ == '__main__':
    data = fetch_data()
    data.to_csv('historical_data.csv', index=False)
