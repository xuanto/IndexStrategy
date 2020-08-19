import os
import tushare as ts
import pandas as pd
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')

# 所有的策略都是纯函数，输入是行情信息，返回operation

def north_money_strategy(trade_information):

    buy_or_sell = True
    shares =
    pass
    operation = (buy_or_sell, shares)
    return operation

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
        
        
