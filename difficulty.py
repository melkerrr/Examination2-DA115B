class Difficulty:
    def __init__(self, level="easy"):
        self.level = level

    def decide_roll_again(self, points, current_player_score):
        if self.level == "easy":
            # When difficulty set to easy the computer always rolls again
            return True
        elif self.level == "hard":
            # When difficulty set to hard the computer rolls again only if it is advantageous
            # e.g. if the current turn's points are less than 15 or the total score is below 80, the computer rolls agian
            return points < 15 or current_player_score + points < 80
        else:
            # default behavior if difficulty level is not recognized
            return True
