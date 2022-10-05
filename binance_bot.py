from emailer import *

import pandas as pd
import sqlalchemy
from binance.client import Client
from binance import BinanceSocketManager
from binanceKeys import *
import asyncio
print("hello binance world")
def createFrame(msg):
	df = pd.DataFrame([msg])
	df = df.loc[:,["s","E","p"]]
	df.columns = ["symbol","Time","Price"]
	df.Price = df.Price.astype(float)
	df.Time = pd.to_datetime(df.Time,unit ="ms")
	return df
client = Client(API_Key,Secret)
bsm = BinanceSocketManager(client)
socket = bsm.trade_socket("BTCGBP")
async def main():
    await socket.__aenter__()
    msg = await socket.recv()
    print(createFrame(msg))
    notify(body=str(createFrame(msg)),subject="Hey Boss, BTC has changed!")
loop = asyncio.get_event_loop()
loop.run_until_complete(main())