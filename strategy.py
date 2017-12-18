#coding=utf-8
from trade import Trade
from data_repository import DataRepository
import tushare as ts
import pandas as pd
import numpy as np
import math


class Strategy(object):
    def __init__(self, code_list, init_cash, starttime, endtime):
        self.starttime = starttime
        self.endtime = endtime
        self.data_repository = DataRepository.get_instance(code_list, starttime, endtime)
        self.code_list = code_list
        self.init_cash = init_cash
        self.cash = init_cash
        self.limited_cash = init_cash/len(code_list)
        self.position_list = {}
        for code in self.code_list:
            self.position_list[code] = 0
        #存储trade对象
        self.trade = Trade()



    def run_simulation(self):

        dr = pd.period_range(start=self.starttime, end=self.endtime, freq='B')
        #按天循环
        for date in dr:
            for code in self.code_list:
                sell_signal, price = self.get_sell_signal(code, str(date))
                direction = -1
                if sell_signal == 1:
                    amount = self.get_sell_amount(code, price)
                    if amount > 0:
                        commission = self.cal_cost_function(price, amount)
                        #更改现金
                        self.cash += price*amount
                        self.cash -= commission
                        #更改持仓
                        self.position_list[code] -= amount
                        #加入trade记录
                        self.trade.add_trade(code, price, amount, str(date), direction, commission)



            for code in self.code_list:
                buy_signal, price = self.get_buy_signal(code, str(date))
                direction = 1
                if buy_signal == 1:
                    amount = self.get_buy_amount(code, price)
                    if amount > 0:
                        commission = self.cal_cost_function(price, amount)
                        #更改现金
                        self.cash -= price*amount
                        self.cash -= commission
                        #更改持仓
                        self.position_list[code] += amount
                        #加入trade记录
                        self.trade.add_trade(code, price, amount, str(date), direction, commission)

    #code='002415' date='2017-01-01' str类型
    def get_sell_signal(self, code, date):

        df = self.data_repository.get_onecode_df(code)
        sell_signal = 0
        price = 0

        if df[df['date'] == date].empty:
            return sell_signal, price
        df = df[df['date'] <= date].tail(2)
        if len(df) == 2 and df.iloc[0]['ma5'] > df.iloc[0]['ma10'] and df.iloc[1]['ma5'] < df.iloc[1]['ma10']:
            sell_signal = 1
            price = df.iloc[1]['open']
        return sell_signal, price

        #以后还要加入判断止盈的方法

    def get_buy_signal(self, code, date):
        df = self.data_repository.get_onecode_df(code)
        buy_signal = 0
        price = 0
        if df[df['date'] == date].empty:
            return buy_signal, price
        df = df[df['date'] <= date].tail(2)
        if len(df) == 2 and df.iloc[0]['ma5'] < df.iloc[0]['ma10'] and df.iloc[1]['ma5'] > df.iloc[1]['ma10']:
            buy_signal = 1
            price = df.iloc[1]['open']
        return buy_signal, price

    def get_sell_amount(self, code, price):
        return self.position_list[code]

    def get_buy_amount(self, code, price):
        if self.position_list[code] == 0:
            amount = math.floor(self.limited_cash/(price*100))*100
            return amount
        else:
            return 0

    def cal_cost_function(self, price, amount):
        commission = price*amount*0.0003
        #最低5元手续费
        if commission > 5:
            return commission
        else:
            return 5