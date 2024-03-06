from player import Player
import random

class HumanPlayer(Player):
    def play_turn(self):
        points = 0
        while True:
            print(f"\n{self.name}'s current score: {self.score}")
            choice = input(f"{self.name}'s turn. Current score: {self.score}\nRoll or Hold? (r/h): ").lower()
            if choice == 'r':
                roll = random.randint(1, 6)
                print(f'{self.name} rolled: {roll}')
                if roll == 1:
                    print('You rolled a 1. Turn ends.')
                    break
                else:
                    points += roll
                    print(f'Points accumulated this turn: {points}')
            elif choice == 'h':
                print(f'{self.name} holds. Points earned: {points}')
                self.update_score(points)
                break
            else:
                print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")