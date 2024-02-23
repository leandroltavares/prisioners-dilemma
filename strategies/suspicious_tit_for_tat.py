from player import Player, Action

class SuspiciousTitForTatPlayer(Player):
    '''Starts by defecting, and defects if the opponent defected on previous round, cooperate otherwise'''
    def next_action(self, previous) -> Action:
        if len(previous) == 0 or previous[-1] == Action.DEFECT:
            return Action.DEFECT
        return Action.COOPERATE
    
    def __repr__(self) -> str:
        return 'Suspicious Tit For Tat'