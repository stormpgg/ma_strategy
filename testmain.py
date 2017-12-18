from strategy import Strategy


if __name__ == '__main__':

    code_list = ['002415', '002416', '000333']
    init_cash = 100000
    starttime = '2014-11-01'
    endtime = '2017-11-30'
    strategy = Strategy(code_list, init_cash, starttime, endtime)
    strategy.run_simulation()
    strategy.trade.output()
