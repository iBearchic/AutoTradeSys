from pybit.unified_trading import HTTP

session = HTTP(testnet=True)

print(session.get_kline(
    category="inverse",
    symbol="BTCUSD",
    interval=60,
    start=1670601600000,
    end=1670608800000,
))

