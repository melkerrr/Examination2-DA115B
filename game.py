import random

from difficulty import Difficulty
from statsmanager import StatsManager

class Game:
    def __init__(self, player1, player2=None, difficulty='easy'):
        self.player1 = player1
        self.player2 = player2
        self.stats_manager = StatsManager()
        self.current_game_over = False
        self.difficulty = Difficulty(difficulty)
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
            if self.player2:
                print(f"\n{self.player2.name}'s current score: {self.player2.score}")
            else:
                print("\nComputer's current score is not idsplayed during its turn.")
    
    def play_turn(self):
        points = 0
        while True:
            self.display_score()
            if self.current_player == self.player1:
                choice = input(f"{self.current_player.name}'s turn. Current score: {self.current_player.score}\nRoll or Hold? (r/h): ").lower()
                if choice == 'r':
                    roll = self.roll_dice()
                    print(f'{self.current_player.name} rolled: {roll}')
                    if roll == 1:
                        print('You rolled a 1. Turn ends.')
                        break
                    else:
                        points += roll
                        print(f'Points accumulated this turn: {points}')
                elif choice == 'h':
                    print(f'{self.current_player.name} holds. Points earned: {points}')
                    self.current_player.update_score(points)
                    break
                else:
                    print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")
            else: # computer's turn
                roll_again = self.difficulty.decide_roll_again(points, self.current_player.score)
                if roll_again:
                    roll = self.roll_dice()
                    print(f'\n{self.current_player.name} rolled: {roll}') 
                    if roll == 1:
                        print('\nThe computer rolled a 1. Turn ends.')
                        break
                    else:
                        points += roll
                        print(f'Points accumulated this turn: {points}')  
                        if points >= 20 or self.current_player.score + points >= 100:
                            print(f'\nThe computer holds. Points earned: {points}')
                            self.current_player.update_score(points)
                            break

    def play_game(self):
        while self.player1.score < 100 and (self.player2 is None or self.player2.score < 100):
            self.play_turn()
            self.switch_player()
        print('\nGame Over!')
        print(f'\n{self.player1.name}: {self.player1.score}')
        if self.player2:
            print(f'{self.player2.name}: {self.player2.score}')
        if self.player1.score > (self.player2.score if self.player2 else 0):
            winner = self.player1.name
        elif self.player2 and self.player2.score > self.player1.score:
            winner = self.player2.name
        else:
            winner = "It's a draw!"
        print(f'Winner: {winner}')

    def quit_game(self):
        self.current_game_over = True