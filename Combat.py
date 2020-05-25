# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:36:36 2020

@author: Eddie
"""
import math

class Combat(object):
    def __init__(self, champion_loader, playeragent, opponentagent):
        self.champion_loader = champion_loader
        self.player_champion = playeragent.bench['c1']
        self.opponent_champion = opponentagent.bench['c1']
    
    def combatTurn(self, ms):        
        if (ms % math.floor(1000/self.player_champion['attack_speed'])) == 0:
            self.update_champions(self.player_champion, self.opponent_champion)
            print('Player champion attacks')
            print(ms)
            print(self.player_champion)
            print(self.opponent_champion)
        # Get champions to fight        
        if (ms % math.floor(1000/self.opponent_champion['attack_speed'])) == 0:
            self.update_champions(self.opponent_champion, self.player_champion)
            print('Opponent champion attacks')
            print(ms)
            print(self.player_champion)
            print(self.opponent_champion)

    def combatPrep(self, player_champion, player_champion_star, opponent_champion, opponent_champion_star):
        player_champion['current_hp'] = player_champion['hp'+player_champion_star]
        player_champion['current_damage'] = player_champion['damage'+player_champion_star]
        opponent_champion['current_hp'] = opponent_champion['hp'+opponent_champion_star]
        opponent_champion['current_damage'] = opponent_champion['damage'+opponent_champion_star]
        
    def combatEnd(self, ):
        if self.player_champion['current_hp'] == 0:
            return 'opponent'
        if self.opponent_champion['current_hp'] == 0:
            return 'player' 
        return False 
        
    def update_champions(self, attacker, defender):
        damage_multiplier = 100/(100+defender['armor'])
        damage = attacker['current_damage']*damage_multiplier
        defender['current_hp'] = max(defender['current_hp'] - damage, 0)

    def run(self):
        #ms stands for milleseconds because actions happen 
        ms = 0
        self.player_champion = self.champion_loader.getChampion(self.player_champion)
        self.opponent_champion = self.champion_loader.getChampion(self.opponent_champion)
        self.combatPrep(self.player_champion, '1', self.opponent_champion, '1')

        while not self.combatEnd() and ms < 50000:
            self.combatTurn(ms)
            ms += 1
        if not self.combatEnd():
            return 'timeout'
        else:
            return self.combatEnd()