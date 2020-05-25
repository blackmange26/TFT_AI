# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:56:44 2020

@author: Eddie
"""

#ToDo: Create a class that holds the board and bench for every player
#Shop has been reverted to all champs to test the DQN implementation

import copy
import random
# from ChampionLoader import ChampionLoader

class Agent(object):
    def __init__(self, name, gold, champion_loader = ChampionLoader()):
        self.board = {### TO DO
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
        self.shop = list(self.champion_loader.data.keys())
#         self.shop = random.sample(list(self.champion_loader.data.keys()), 5)
        self.hp = 100
        
    ### because we haven't implemented the full game mechanics yet, to test the DQN the mechanic will be only 1 champion at a time    
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
            ### temporary
            self.bench['c1'] = champion_to_buy
#             position_for_champion = next((x for x in self.bench if self.bench[x] == 'Empty'))
#             self.bench[position_for_champion] = champion_to_buy
#             self.shop.remove(champion_to_buy)
            self.gold = self.gold - self.champion_loader.getChampion(champion_to_buy)['cost']

    def getStateCopy(self):
        return copy.deepcopy(self.state)

    def getAction(self, gameState):
        pass

    ### auto parameter allows for a shop refresh without costing gold
    def shopRefresh(self, auto=False):
        if self.gold < 2:
            return False
        elif auto:
            self.shop = list(self.champion_loader.data.keys())
#             self.shop = random.sample(list(self.champion_loader.data.keys()), 5)
#             self.gold = self.gold - 2
            return True
        else:
            self.shop = list(self.champion_loader.data.keys())
#             self.shop = random.sample(list(self.champion_loader.data.keys()), 5)
            self.gold = self.gold - 2
            return True
        
    def benchRefresh(self):
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