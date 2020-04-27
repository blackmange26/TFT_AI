# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:11:29 2020

@author: Eddie
"""

from ChampionLoader import ChampionLoader
from Game import Game

Game = Game(ChampionLoader(), 'Aatrox', 'Fiora')
print(Game.run())
# print(Game.r)
# Champ_Object = ChampionLoader()
# print(Champ_Object.getChampion('Jinx'))