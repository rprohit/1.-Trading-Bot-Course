import pprint
import tkinter as tk
import logging

import config
from connectors.binance_future import BinanceFuturesClient
from connectors.bitmex import get_contracts

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':
    binance = BinanceFuturesClient(config.API_KEY,config.API_SECRET,False)
    #pprint.pprint(binance.get_balances())
    #pprint.pprint(binance.place_order("BTCUSDT","BUY",0.01,"LIMIT",20000,"GTC"))
    #pprint.pprint(binance.cancel_order(40310794776,"BTCUSDT"))
    root = tk.Tk()
    root.mainloop()
