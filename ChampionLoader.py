# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:21:26 2020

@author: Eddie
"""

import pandas as pd
import collections

class ChampionLoader(object):
    def __init__(self):
        self.df = pd.read_csv('./data/champion_stats.csv')
        self.data = collections.defaultdict(dict)
        for _, r in self.df.iterrows():
            id = r['champion']
            self.data[id] = {
                'champion': r['champion'],
                'origin': r['origin'],
                'class': r['class'],
                'cost': None if pd.isnull(r['cost']) else int(r['cost']),
                'hp1': None if pd.isnull(r['hp1']) else int(r['hp1']),
                'hp2': None if pd.isnull(r['hp2']) else int(r['hp2']),
                'hp3': None if pd.isnull(r['hp3']) else int(r['hp3']),
                'dps1': None if pd.isnull(r['dps1']) else int(r['dps1']),
                'dps2': None if pd.isnull(r['dps2']) else int(r['dps2']),
                'dps3': None if pd.isnull(r['dps3']) else int(r['dps3']),
                'attack_speed': None if pd.isnull(r['attack_speed']) else int(r['attack_speed']),
                'damage1': None if pd.isnull(r['damage1']) else int(r['damage1']),
                'damage2': None if pd.isnull(r['damage2']) else int(r['damage2']),
                'damage3': None if pd.isnull(r['damage3']) else int(r['damage3']),
                'range': None if pd.isnull(r['range']) else int(r['range']),
                'armor': None if pd.isnull(r['armor']) else int(r['armor']),
                'magic_resist': None if pd.isnull(r['magic_resist']) else int(r['magic_resist'])
            }
        del self.df

    def getChampion(self, champion):
        return self.data[champion]