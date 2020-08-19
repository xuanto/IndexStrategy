import os
import tushare as ts
import pandas as pd
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')

# 所有的策略都是纯函数，输入是行情信息，返回operation

def north_money_strategy(market_information):
    north_money_today = market_information.today.north_money + ajust_factor
    if north_money_today < 30 and north_money_today > -20:
        # no operation
        operate_code = 0
        operation = (operate_code, 0)
        return operation
    if north_money_today < 0:
        shares = - (north_money_today * 100 // market_information.north_money_postion)
        operate_code = -1
        operation = (operate_code, shares)
        return operation
    if north_money_today > 0:
        shares = (north_money_today * 100 // market_information.north_money_postion)
        operate_code = (operate_code, shares)
        operation = (operate_code, shares)
        return operation

def avg_5_strategy(market_information):
    """5日均线策略，当前价格低于均线时买入，高于时卖出"""
    pass

def smarter_aip(market_information):
    """逢跌定投策略，跌了就买入"""
    pass
        


def synthesis_strategy(market_information):
    """综合策略"""
    north_money_operation = north_money_strategy(market_information)
    avg_operation = avg_5_strategy(market_information)
    pass
        
        
