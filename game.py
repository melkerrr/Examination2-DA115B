"""
Module containing the Game class representing the game logic.
"""

import random
from difficulty import Difficulty
from statsmanager import StatsManager

class Game:
    """
    Class representing the game logic.
    """

    def __init__(self, player1, player2=None, difficulty="easy"):
        """
        Initialize the Game object.

        Args:
            player1 (Player): The first player.
            player2 (Player, optional): The second player. Defaults to None.
            difficulty (str, optional): The difficulty level. Defaults to "easy".
        """
        self.player1 = player1
        self.player2 = player2
        self.stats_manager = StatsManager()
        self.current_game_over = False
        self.difficulty = Difficulty(difficulty)
        self.current_player = player1

    def  play_turn_manual(self):
        """
        Manually play turn
        """
        points = 0
        while True:
            self.display_score()
            choice = input(f"{self.current_player.name}'s turn. Current score: {self.current_player.score}\nRollor Hold? (r/h): ").lower()
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

    def switch_player(self):
        """
        Switch the current player.
        """
        if self.current_player == self.player1:
            self.current_player = self.player2 if self.player2 else self.player1
        else:
            self.current_player = self.player1

    def roll_dice(self):
        """
        Simulate rolling a six-sided dice.

        Returns:
            int: The result of the dice roll.
        """
        return random.randint(1, 6)

    def display_score(self):
        """
        Display the current player's score.
        """
        if self.current_player == self.player1:
            print(f"\n{self.player1.name}'s current score: {self.current_player.score}")
        elif self.current_player == self.player2:
            if self.player2:
                print(f"\n{self.player2.name}'s current score: {self.player2.score}")
            else:
                print("\nComputer's current score is not displayed during its turn.")

    def play_turn(self):
        """
        Play a turn of the game.
        """
        points = 0
        while True:
            self.display_score()
            if self.current_player == self.player1:
                choice = input(
                    f"{self.current_player.name}'s turn. Current score: {self.current_player.score}\nRoll or Hold? (r/h): "
                ).lower()
                if choice == "r":
                    roll = self.roll_dice()
                    print(f"{self.current_player.name} rolled: {roll}")
                    if roll == 1:
                        print("You rolled a 1. Turn ends.")
                        break
                    else:
                        points += roll
                        print(f"Points accumulated this turn: {points}")
                elif choice == "h":
                    print(f"{self.current_player.name} holds. Points earned: {points}")
                    self.current_player.update_score(points)
                    break
                else:
                    print("Invalid choice! Please choose 'r' to roll or 'h' to hold.")
                if self.current_player.score >= 100:
                    self.current_game_over = True
                    break            
            else:  # computer's turn
                if self.current_player.score >= 100:
                    print(f'\n{self.current_player.name} holds. Points earned: {points}')
                    self.current_game_over = True
                    break
                roll_again = self.difficulty.decide_roll_again(
                    points, self.current_player.score
                )
                if roll_again:
                    roll = self.roll_dice()
                    print(f'\n{self.current_player.name} rolled: {roll}')
                    if roll == 1:
                        print('\nThe computer rolled a 1. Turn ends.')
                        break
                    else:
                        points += roll
                        print(f'Points accumulated this turn: {points}')
                        if points >= 20:
                            if self.current_player.score + points >= 100:
                                print(f'\nThe computer holds. Points earned: {points}')
                                self.current_game_over = True
                            else:
                                print('\nThe computer decides to hold.')
                                self.current_player.update_score(points)
                                break
                        else:
                            print('\nThe computer decides to roll again.')
            if self.current_player.score >= 100:
                self.current_game_over = True
                break

    def play_game(self):
        """
        Play the game until one of the players wins.
        """
        while not self.current_game_over:
            self.play_turn()
            if self.player1.score >= 100 or (self.player2 and self.player2.score >= 100):
                self.current_game_over = True
        print("\nGame Over!")
        print(f"\n{self.player1.name}: {self.player1.score}")
        if self.player2:
            print(f"{self.player2.name}: {self.player2.score}")
        if self.player1.score > (self.player2.score if self.player2 else 0):
            winner = self.player1.name
        elif self.player2 and self.player2.score > self.player1.score:
            winner = self.player2.name
        else:
            winner = "It's a draw!"
        print(f"Winner: {winner}")

    def quit_game(self):
        """
        Quit the game.
        """
        self.current_game_over = True
