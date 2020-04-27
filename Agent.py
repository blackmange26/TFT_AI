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
        self.gold = gold
        self.champion_loader = champion_loader
        self.shop = random.sample(list(self.champion_loader.data.keys()), 5)

    def getChamp(self):
        return self.champion

    def getStateCopy(self):
        return copy.deepcopy(self.state)

    def getAction(self, gameState):
        pass
