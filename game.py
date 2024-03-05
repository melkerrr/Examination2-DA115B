import random

class Game:
    def __init__(self, player1, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def roll_dice(self):
        return random.randint(1, 6)
    
    def play_turn(self):
        points = 0
        roll = self.roll_dice()
        while roll != 1:
            points += roll
            roll = self.roll_dice()
        self.current_player.update_score(points)

    def play_game(self):
        while self.player1.score < 100 and self.player2.score < 100:
            self.play_turn()
            self.switch_player()