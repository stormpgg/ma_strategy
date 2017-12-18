#coding=utf-8
import tushare as ts
import pandas as pd
import numpy as np


class Profolio(object):
    def __init__(self, init_cash, code_list):
        self.code_list = code_list
        self.init_cash = init_cash
        self.cash = 0
        self.security_in_hand = {}


    def set_security_list(self, code_list):
        self.code_list = code_list
        for code in self.code_list:
            self.stock_in_hand[code] = 0

    def set_init_cash(self, cash):
        self.init_cash = cash
        self.cash = cash