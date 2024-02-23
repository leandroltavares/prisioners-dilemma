from player import Player, Action

class TitForTatPlayer(Player):
    '''Starts by cooperating, and defects if the opponent defected on previous round'''
    def next_action(self, previous) -> Action:
        if len(previous) and previous[-1] == Action.DEFECT:
            return Action.DEFECT
        return Action.COOPERATE
    
    def __repr__(self) -> str:
        return 'Tit For Tat'