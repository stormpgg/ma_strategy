#coding=utf-8
import tushare as ts
import pandas as pd
import numpy as np
import math


class DataRepository(object):

    __instance = None

    def __init__(self, code_list, starttime, endtime):
        self.all_data = {}
        for code in code_list:
            df = ts.get_k_data(code, starttime, endtime)
            df['ma5'] = df['close'].rolling(5).mean()
            df['ma10'] = df['close'].rolling(10).mean()
            df.dropna(how='any')
            self.all_data[code] = df

    @classmethod
    def get_instance(cls, code_list, starttime, endtime):
        if DataRepository.__instance is None:
            DataRepository.__instance = DataRepository(code_list, starttime, endtime)
            return DataRepository.__instance
        else:
            return DataRepository.__instance

    def get_onecode_df(self, code):
        return self.all_data[code]