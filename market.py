import tushare as ts
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')

class Chives(object):
    """韭菜，根据operation进行交易"""
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
        operate_code, shares = opration
        if operate_code == 0:
            return
        elif operate_code == 1:
            pass
        elif operate_code == -1:
            pass


class Market(object):
    """市场，提供行情信息"""
    def __init__(self):
        super(Market, self).__init__()
        today = datetime.date.today()
        # YYYYMMDD
        self.today = datetime.date.today().strftime("%Y%m%d")
        self.yesterday = today - datetime.timedelta(days=1)
        self.pro = ts.pro_api()

        self.data_path = conf.get_string("data.north_money_hist_file")
        if os.file_exist(data_path)
            self.hist_data = pd.read_csv(self.data_path)
        else:
            self.hist_data = self.__update_hist_data()
        # pro = ts.pro_api()
        # north_money_raw = pro.moneyflow_hsgt(start_date='20180101', end_date='20181231')
        # days, _ = north_money_raw.shape

    #  根据历史数据计算北向资金增长因子
    def get_increate_factor(self):
        m_inf_north_money_position = self.north_money_hist_data.north_money.sum()
        pass

    def __get_hsgt(self, date1, date2):
        return  self.pro.moneyflow_hsgt(start_date=date1, end_date=date2)

    # 生成北向数据
    def __generate_hist_data(self):
        date1 = self.yesterday - datetime.timedelta(days=300)
        date2 = self.yesterday
        df = self.__get_hsgt(date1, date2)
        for _ in range(8):
            date2 = date1 - datetime.timedelta(days=1)
            date1 = date1 - datetime.timedelta(days=300)
            df.append(self.__get_hsgt(date1, date2))
            print(df.shape)
        df = df.sort_values(by="trade_date")
        df.to_csv(self.data_path)
        return df

    # 更新北向数据
    def __update_hist_data(self):
        x = self.north_money_hist_data.tail(1).trade_date.item()
        x = [int(x[:4]), int(x[4:6]), int(x[6:8])]
        YYYYMMDD = datetime.datetime(*x)
        
        date1 = self.yesterday - datetime.timedelta(days=300)
        date2 = self.yesterday
        df = self.__get_hsgt(date1, date2)
        for _ in range(8):
            date2 = date1 - datetime.timedelta(days=1)
            date1 = date1 - datetime.timedelta(days=300)
            df.append(self.__get_hsgt(date1, date2))
            print(df.shape)
        df.to_csv(self.data_path)
        return df

    # [core function] 估算北向资金的持仓，输出北向资金的持仓情况
    def get_north_money_position(self):
        pass

    # [core function] 返回行情信息:market_information
    def get_market_information(self):
        pro = ts.pro_api()
        df = pro.daily(ts_code='000001.SZ', start_date='20180701', end_date='20180718')


        north_money_position = self.get_north_money_position()     



# evaluation
def eval(self, strategy, start_date, end_date):
    pass



if __name__ == '__main__':
    print("testing ... ")
    chive = Chives()
    market = Market()

    

