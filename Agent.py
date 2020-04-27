# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:56:44 2020

@author: Eddie
"""

#ToDo: Create a class that holds the board and bench for every player

import copy
import random
from ChampionLoader import ChampionLoader

class Agent(object):
    def __init__(self, name, champion, gold, champion_loader = ChampionLoader()):
        self.champion = champion
        self.board = {
        }
        self.bench = {'c1': 'Empty',
                'c2': 'Empty',
                'c3': 'Empty',
                'c4': 'Empty',
                'c5': 'Empty',
                'c6': 'Empty',
                'c7': 'Empty',
                'c8': 'Empty',
                'c9': 'Empty'
        }
        self.gold = gold
        self.champion_loader = champion_loader
        self.shop = random.sample(list(self.champion_loader.data.keys()), 5)
        
    def buyChampion(self, champion_to_buy):
        ### Check if the bench is full
        if "Empty" not in self.bench.values():
            return 1
        ### Check if shop has the champion
        elif champion_to_buy not in self.shop:
            return 2
        ### Check if player has enough gold
        elif self.champion_loader.getChampion(champion_to_buy)['cost'] > self.gold:
            return 3
        else:
            position_for_champion = next((x for x in self.bench if self.bench[x] == 'Empty'))
            self.bench[position_for_champion] = champion_to_buy
            self.shop.remove(champion_to_buy)

    def getChamp(self):
        return self.champion

    def getStateCopy(self):
        return copy.deepcopy(self.state)

    def getAction(self, gameState):
        pass

    def shopRefresh(self):
        if self.gold < 2:
            return False
        else:
            self.shop = random.sample(list(self.champion_loader.data.keys()), 5)
            self.gold = self.gold - 2
            return True