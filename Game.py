# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:36:36 2020

@author: Eddie
"""

class Game(object):
    def __init__(self, champion_loader, player_champion, opponent_champion):
        self.champion_loader = champion_loader
        self.player_champion = player_champion
        self.opponent_champion = opponent_champion 
    
    def combat(self):
        # Get champions to fight        
        self.update_champions(self.player_champion, self.opponent_champion)
        self.update_champions(self.opponent_champion, self.player_champion)

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
        counter = 0
        self.player_champion = self.champion_loader.getChampion(self.player_champion)
        self.opponent_champion = self.champion_loader.getChampion(self.opponent_champion)
        self.combatPrep(self.player_champion, '1', self.opponent_champion, '1')

        while not self.combatEnd() and counter < 500:
            self.combat()
            counter += 1
            print(counter)
            print(self.player_champion)
            print(self.opponent_champion)
        if not self.combatEnd():
            return 'timeout'
        else:
            return self.combatEnd()