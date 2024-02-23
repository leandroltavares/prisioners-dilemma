from enum import Enum

class Action(Enum):
    COOPERATE = 1
    DEFECT = 2

class Player:
    def __init__(self):
        pass

    def next_action(self, previous) -> Action:
        pass