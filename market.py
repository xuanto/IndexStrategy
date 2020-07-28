import tushare as ts

class Chives(object):
    """docstring for Chives"""
    def __init__(self, leverage=100, total_money=10000):
        super(Chives, self).__init__()
        self.init_leverage = leverage
        self.total_money = total_money

        self.leverage = self.init_leverage
        self.available_money = total_money
        self.share = 0
        self.profit = 0
        self.one_hand = (1 / leverage) * self.available_money

    def get_float_profit(self, price):
        return (self.available_money + self.share * price) - self.total_money

    def get_real_profit(self):
        return self.profit

    def buy(self, n, price):
        if n <= self.leverage: 
            self.leverage -= n
            self.share += (n * self.one_hand) / price
            self.available_money -= n * self.one_hand

    def sell(self, n, price):
        if (n + self.leverage <= self.init_leverage):
            sell_share = n / ( self.init_leverage - self.leverage) * self.share
            self.share -= sell_share
            self.available_money += sell_share * price
            self.leverage += n
            self.profit += self.get_float_profit(price)

if __name__ == '__main__':
    # pro = ts.pro_api()
    # north_money_raw = pro.moneyflow_hsgt(start_date='20180101', end_date='20181231')
    # days, _ = north_money_raw.shape


    print("testing ... ")
    chive = Chives()
    chive.buy(2, 1)
    chive.buy(3, 1.2)
    print(chive.get_float_profit(2.8))
    chive.sell(2, 1.2)
    print(chive.get_real_profit())
    chive.sell(3, 0.1)
    print(chive.get_real_profit())

