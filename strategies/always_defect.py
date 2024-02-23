from player import Player, Action

class AlwaysDefectPlayer(Player):
    '''Always Defects'''
    def next_action(self, _) -> Action:
        return Action.DEFECT
    
    def __repr__(self) -> str:
        return 'Always Defect'