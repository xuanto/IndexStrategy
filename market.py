import tushare as ts
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')

class Chives(object):
    """韭菜"""
    def __init__(self, leverage=100, total_money=10000):
        super(Chives, self).__init__()
        self.init_leverage = conf.get_int("trade.leverage")
        self.total_money = conf.get_int("trade.total_money")
        self.freeze_time = conf.get_int("rules.freeze_time")

        self.leverage = self.init_leverage
        self.available_money = total_money
        self.share = 0
        self.profit = 0
        self.one_hand = (1 / leverage) * self.available_money

        self.position = [] # a list like [(trade_date, share), ... ]
        self.total_share = 0
        self.free_share = 0

    def get_float_profit(self, price):
        return (self.available_money + self.share * price) - self.total_money

    def get_real_profit(self):
        return self.profit

    def __update_free_share(self, time):
        while (self.position and self.__is_frozen(self.position[-1], time)):
            time, share = self.position.pop(-1)
            self.free_share += share
            self.total_share -= share
        return

    def __is_frozen(self, position_item, time):
        trade_date, share = position_item
        return (time - self.freeze_time) > trade_date

    def __buy(self, money, price, time):
        share = money / price
        return (share, time)

    def __sell(self, money, price):
        return share * price

    # core function, opration is a data structure
    def operate(self, opration):
        pass


class Market(object):
    """市场"""
    def __init__(self, strategy):
        super(Market, self).__init__()
        self.chive = Chives()
        self.strategy = strategy

        # pro = ts.pro_api()
        # north_money_raw = pro.moneyflow_hsgt(start_date='20180101', end_date='20181231')
        # days, _ = north_money_raw.shape

    def eval(self, strategy, start_date, end_date):
        pass

    def hangqing(self, ):
        pro = ts.pro_api()
        df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')





if __name__ == '__main__':
    print("testing ... ")
    chive = Chives()
    chive.buy(2, 1)
    chive.buy(3, 1.5)
    print(chive.get_float_profit(2.8))
    chive.sell(2, 1.2)
    print(chive.get_real_profit())
    chive.sell(3, 0.1)
    print(chive.get_real_profit())

