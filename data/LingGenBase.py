# coding:utf-8
from data.Database import Database


class LingGen(Database):
    def __init__(self):
        super(LingGen, self).__init__()
        self.name = 'LingGen.txt'


linggen_base = LingGen()
