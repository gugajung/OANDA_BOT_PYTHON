import pandas as pd
import matplotlib.pyplot as plt
import handle_data as hd
from mpl_finance import candlestick2_ohlc
import os


def chart(plan, id, asset, time, date):

        name = id + "_" + str(time)

        total = 0
        for i in plan.keys():
                if i == id:
                        for ii in plan.get(i)['strat'].keys():
                                total += 1
                                df = hd.handler().candle_data(asset, plan.get(i)['strat'][ii], 50)

                                fig, ax = plt.subplots(figsize=(15,10))
                                candlestick2_ohlc(ax, df.open, df.high, df.low, df.close, width=0.5, colorup='g', colordown='r')
                                ax.set_title(f"{asset} with {plan.get(i)['strat'][ii]} Minutes Candle",fontsize=18)
                                
                                if not os.path.exists(f'./DATA/charts/{date}'):
                                        os.makedirs(f'./DATA/charts/{date}')

                                plt.savefig(f'./DATA/charts/{date}/{name}_{total}.svg')
                                plt.clf()


