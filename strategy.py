import tushare as ts
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')


class NorthMoneyStrategy(object):
    """北向资金策略：通过复制北向资金的持仓来控制仓位"""
    def __init__(self, arg):
        super(NorthMoneyStrategy, self).__init__()
        self.arg = arg


    #  根据历史数据计算北向资金增长因子
    def get_increate_factor(self):
        pass

    # 计算北向资金的持仓
    def get_north_money_position(self):
        pass

    # 更新北向数据
    def __update_hist_data(self):
        pass


    # 根据北向资金当天的流入流出，计算出持仓策略
    def opertation(self, money_flow):




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
        
        
