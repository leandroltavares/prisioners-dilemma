import os
import importlib
import argparse
import numpy as np

from itertools import combinations_with_replacement
from player import Player, Action

DEFAULT_ROUNDS = 100
SCORE_MATRIX = {(Action.COOPERATE, Action.COOPERATE): (3, 3),
                (Action.DEFECT, Action.COOPERATE): (5, 0),
                (Action.COOPERATE, Action.DEFECT): (0, 5),
                (Action.DEFECT, Action.DEFECT): (1, 1)}

class Simulation:
    def __init__(self, rounds):
        self.rounds = rounds
        self.players = []
        self.scores = None

    def run(self):
        self.load_strategies()
        for r in range(self.rounds):
            self.run_round(r)

    def run_round(self, round):
        print(f'Running round: {round}')
        for (i1, p1), (i2, p2) in combinations_with_replacement(enumerate(self.players), 2):
            p1_action = p1.next_action(self.actions[:round, i1, i2])
            p2_action = p2.next_action(self.actions[:round, i2, i1])
            p1_score, p2_score = self.compute_score(p1_action, p2_action)
            print(f'[P{i1}][{p1}] => [{p1_action}] vs [P{i2}][{p2}] => [{p2_action}]: {p1_score, p2_score}')
            self.actions[round, i1, i2] = p2_action
            self.actions[round, i2, i1] = p1_action
            self.scores[i1] += p1_score
            self.scores[i2] += p2_score
    
    def compute_score(self, p1_action, p2_action):
        return SCORE_MATRIX[(p1_action, p2_action)]
        
    def load_strategies(self):
        strategy_files = [f[:-3] for f in os.listdir('strategies') if f.endswith('.py') and not f.startswith('__init__')]

        for strategy_file in strategy_files:
            module_name = f'strategies.{strategy_file}'
            module = importlib.import_module(module_name)
            
            classes = [cls for cls in dir(module) if 
                       isinstance(getattr(module, cls), type) 
                       and issubclass(getattr(module, cls), Player)
                       and cls != 'Player']
            
            for player_class in classes:
                player_instance = getattr(module, player_class)()
                self.players.append(player_instance)
        
        self.scores = np.zeros(len(self.players), dtype=int)
        self.actions = np.empty((self.rounds, len(self.players), len(self.players)), dtype=Action)
        
        print(f'The following players were loaded {self.players}')

    def print_final_score(self):
        final_scores = dict(zip(self.players, self.scores))
        for k, v in sorted(final_scores.items(), key=lambda item: item[1], reverse=True):
            print(f'[{k}]: {v}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rounds", help="Number of rounds", type=int)
    args = parser.parse_args()
 
    s = Simulation(args.rounds or DEFAULT_ROUNDS)
    s.run()
    s.print_final_score()
