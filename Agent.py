# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:56:44 2020

@author: Eddie
"""

#ToDo: Create a class that holds the boad and bench for every player

import copy

class Agent(object):
    def __init__(self, name, champion):
        self.champion = champion
        self.board = {
        }

    def getChamp(self):
        return self.champion

    def getStateCopy(self):
        return copy.deepcopy(self.state)

    def getAction(self, gameState):
        pass
