from player import Player, Action

class AlwaysCooperatePlayer(Player):
    '''Always Cooperates'''
    def next_action(self, previous) -> Action:
        return Action.COOPERATE
    
    def __repr__(self) -> str:
        return 'Always Cooperate'