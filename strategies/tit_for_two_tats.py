from player import Player, Action

class TitForTatPlayer(Player):
    '''Starts by cooperating, and defects if the opponent defected on 2 previous rounds in a row'''
    def next_action(self, previous) -> Action:
        if len(previous) > 1 and previous[-1] == Action.DEFECT and previous[-2] == Action.DEFECT:
            return Action.DEFECT
        return Action.COOPERATE
    
    def __repr__(self) -> str:
        return 'Tit For Two Tats'