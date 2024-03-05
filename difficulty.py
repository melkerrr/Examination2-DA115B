import random

class Difficulty:
    def __init__(self, level='easy'):
        self.level = level

    def decide_roll_again(self, points, current_player_score):
        if self.level == 'easy':
            return random.choice([True, False])
        elif self.level == 'hard':
            return points < 20 or current_player_score + points < 100
        else:
            return True # the default behavior if difficulty level is not recognized