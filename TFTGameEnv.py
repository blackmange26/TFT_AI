# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 23:36:36 2020

@author: Eddie
"""

# from Combat import Combat

class TFTGameEnv(py_environment.PyEnvironment):
    def __init__(self, playeragent, opponentagent, championloader):
        
        ### the action space here includes every champ, purchase XP, re-roll, and end turn
        self._action_spec = array_spec.BoundedArraySpec(shape=(), dtype=np.int32, minimum=0, maximum=100, name='action')

        ### the observation space here includes all the champs in the store as well as all owned champs
        self._observation_spec = array_spec.BoundedArraySpec(shape=(1,), dtype=np.int32, minimum=0, name='observation')
        
        ### this is the reward
        self.reward = 0
        
        ### this is the episode-end and game-end check
        self._game_ended = False
        self._turn_ended = False
        
        ### these are the agents that are used
        self.playeragent = playeragent
        self.opponentagent = opponentagent
        
        ### this is the champion loader
        self.championloader = championloader
        
    def action_spec(self):
        return self._action_spec
    def observation_spec(self):
        return self._observation_spec
    
    ### ### Reset the entire game. Set the HP to 100, bench to empty, refresh shop, reset gold
    def _reset(self):
        self.playeragent.gold = 100
        self.playeragent.shopRefresh(auto=True)
        self.playeragent.benchRefresh()
        self.playeragent.hp = 100
        self.opponentagent.gold = 100
        self.opponentagent.shopRefresh(auto=True)
        self.opponentagent.benchRefresh()
        self.opponentagent.hp = 100
        self.reward = 0
        self._game_ended = False
        return ts.restart(np.array([self.reward], dtype=np.int32))
    
    def _reward(self):
        ### this way, the lower the opponent hp, the higher the reward
        return self.playeragent.gold + (100 - self.opponentagent.hp) + self.playeragent.hp

    def _take_action(self, action):
        ### ### The next statements take in to account every action outcome.
        ### 0 means end turn, and if hp is 0 at the end then end game. loser loses 10 hp.
        ### 1 is re-roll
        ### 2 is purchase XP
        ### 3+ is purchase champions
        if action == 0:
            self._turn_ended = True
            combat_instance = Combat(self.championloader, self.playeragent, self.opponentagent)
            winner = combat_instance.run()
            if winner == 'opponent':
                self.playeragent.hp = self.playeragent.hp - 10
            elif winner == 'player':
                self.opponentagent.hp = self.opponentagent.hp - 10
            if self.playeragent.hp == 0 or self.opponentagent.hp == 0:
                self._game_ended = True

        elif action == 1:
            self.agent.shopRefresh(auto=False)          
        ### TO- DO:elif action == 2:
            ### TO-DO
        elif action > 2 and action <= 96:
            champion_to_buy = self.championloader.getChampion_idx(action-3)['champion'] ### -3 here to account for actions 0 1 2
            print(champion_to_buy)
            self.playeragent.buyChampion(champion_to_buy)
        else:
            raise ValueError('Action not recognized')

    
    def _step(self, action):
        ### take the action
        self._take_action(action)
        
        if self._game_ended:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self.reset()
        
        reward = self._reward()
        
        ### ### This is the calculation of the reward after the turn ends.
        if self._turn_ended:
            return ts.termination(np.array([self.reward], dtype=np.int32), reward)
        else:
            return ts.transition(np.array([self.reward], dtype=np.int32), reward=0.0, discount=1.0)