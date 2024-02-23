import random
from player import Player, Action

class RandomPlayer(Player):
    '''Randomly Defects'''
    def next_action(self, _) -> Action:
        return random.choice([Action.COOPERATE, Action.DEFECT])
    
    def __repr__(self) -> str:
        return 'Random'