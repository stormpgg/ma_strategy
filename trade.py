#coding=utf-8


class Trade(object):

    def __init__(self):
        self.entry_price = 0
        self.exit_price = 0
        self.stop_loss_price = 0
        self.profit_target_price = 0
        self.commission_rate = 0
        self.commission = 0
        self.profit = 0
        self.quantity = 0
        self.entry_time = 0
        self.exit_time = 0
        self.direction_type = 0
        self.trade_list = []

    def add_trade(self, code, price, amount, date, direction, commission):
        one_trade = [date, code, price, amount, direction, commission]
        self.trade_list.append(one_trade)

    def sharp(self):
        pass

    def maxdd(self):
        pass

    def winrate(self):
        pass

    def total_profit(self):
        pass

    def output(self):
        with open('./traderesult.txt', 'a', encoding='utf-8') as f:
            for trade in self.trade_list:
                f.write('%s\n'%trade)