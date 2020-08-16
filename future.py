import tushare as ts
import pytorch as tc
from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('configs/basic.conf')


# future work： 引入深度强化学习进行策略决策 , future work
class DQN(object):
    """docstring for DQN"""
    def __init__(self, arg):
        super(DQN, self).__init__()
        self.arg = arg
        pass
        