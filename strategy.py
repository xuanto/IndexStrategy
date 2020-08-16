import os
import tushare as ts
import pandas as pd
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')

class Operation(object):
    """数据结构，买入或者卖出"""
    def __init__(self, arg):
        super(Operation, self).__init__()
        self.arg = arg

    # 或许可以直接用更简单的东西代替



class NorthMoneyStrategy(object):
    """北向资金策略：通过复制北向资金的持仓来控制仓位"""
    def __init__(self, arg):
        super(NorthMoneyStrategy, self).__init__()
        today = datetime.date.today()
        self.yesterday = today - datetime.timedelta(days=1)
        self.pro = ts.pro_api()

        self.data_path = conf.get_string("data.north_money_hist_file")
        if os.file_exist(data_path)
            self.hist_data = pd.read_csv(self.data_path)
        else:
            self.hist_data = self.__update_hist_data()

    #  根据历史数据计算北向资金增长因子
    def get_increate_factor(self):
        pass

    def __get_hsgt(self, date1, date2):
        return  self.pro.moneyflow_hsgt(
                    start_date=date1.strftime("%Y%m%d"),
                    end_date=date2.strftime("%Y%m%d")
                )

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

    # 估算北向资金的持仓，核心功能。输出北向资金的持仓情况
    def get_north_money_position(self):
        pass

    # 根据北向资金的持仓，计算出操作策略：返回一个Operation
    def opertation(self, money_flow):
        pass



class AvgLinetrategy(object):
    """均线策略，当前价格低于均线时买入，高于时卖出"""
    def __init__(self, arg):
        super(AvgLineStrategy, self).__init__()
        self.arg = arg



class SmarterAIP(object):
    """逢跌定投策略，跌了就买入"""
    def __init__(self, arg):
        super(SmarterAIP, self).__init__()
        self.arg = arg
        


class SynthesisStrategy(object):
    """综合策略"""
    def __init__(self, arg):
        super(SynthesisStrategy, self).__init__()
        self.arg = arg
        
        
