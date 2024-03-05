import random

class Game:
    def __init__(self, player1, player2=None):
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2 if self.player2 else self.player1
        else:
            self.current_player = self.player1

    def roll_dice(self):
        return random.randint(1, 6)
    
    def display_score(self):
        if self.current_player == self.player1:
            print(f"\n{self.player1.name}'s current score: {self.current_player.score}")
        elif self.current_player == self.player2:
            print(f"\n{self.player2.name}'s current score: {self.player2.score}")
    
    def play_turn(self):
        points = 0
        while True:
            self.display_score()
            choice = input(f"{self.current_player.name}'s turn. Current score: {self.current_player.score}\nRoll or Hold? (r/h): ").lower()
            if choice == 'r':
                roll = self.roll_dice()
                print(f'{self.current_player.name} rolled: {roll}')
                if roll == 1:
                    print('You rolled a 1. Turn ends.')
                    break
                else:
                    points += roll
                    print(f'Points accumulated this turm: {points}')
            elif choice == 'h':
                print(f'{self.current_player.name} holds. Points earned: {points}')
                self.current_player.update_score(points)
                break
            else:
                print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")

    def play_game(self):
        while self.player1.score < 100 and (self.player2 is None or self.player2.score < 100):
            self.play_turn()
            self.switch_player()