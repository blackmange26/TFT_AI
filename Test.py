# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:11:29 2020

@author: Eddie
"""

import tensorflow as tf
from tf_agents.agents.dqn import dqn_agent

from ChampionLoader import ChampionLoader
from Game import Game
from Agent import Agent
# Agent = Agent('Eddie', 'Aatrox', 10)

print(Agent.shop)
print(Agent.bench.values())
print(Agent.buyChampion('Katarina'))

# Game = Game(ChampionLoader(), 'Aatrox', 'Fiora')
# print(Game.run())
# print(Game.r)
# Champ_Object = ChampionLoader()
# print(Champ_Object.getChampion('Jinx'))