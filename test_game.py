import unittest
from unittest.mock import patch
from game import Game
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.game = Game(self.player1, self.player2)

    def test_play_turn_manual(self):
        # Test play_turn_manual method for both players
        with patch("builtins.input", side_effect=["r", "h", "r", "h"]):
            # Test for player 1
            self.game.play_turn_manual()
            self.assertTrue(self.player1.score in range(7))  # Player 1's score should be within 0-6

            # Test for player 2
            self.game.current_player = self.player2
            self.game.play_turn_manual()
            self.assertTrue(self.player2.score in range(7))  # Player 2's score should be within 0-6

    def test_play_turn_computer_roll_one(self):
        # Test play_turn method when the computer rolls a 1
        self.game.current_player = self.player2  # Set current player as the computer
        with patch("game.Game.roll_dice", return_value=1), patch("builtins.print") as mock_print:
            self.game.play_turn()
            mock_print.assert_called_with("\nThe computer rolled a 1. Turn ends.")


    def test_play_turn_display_score(self):
        # Test display_score method for both players
        with patch("builtins.print") as mock_print:
            # Display score for player 1
            self.game.display_score()
            mock_print.assert_called_with(f"\n{self.player1.name}'s current score: {self.player1.score}")

            # Display score for player 2
            self.game.current_player = self.player2
            self.game.display_score()
            mock_print.assert_called_with(f"\n{self.player2.name}'s current score: {self.player2.score}")

    def test_quit_game(self):
        # Test quit_game method
        self.assertFalse(self.game.current_game_over)
        self.game.quit_game()
        self.assertTrue(self.game.current_game_over)

    def test_switch_player(self):
        # Test switch_player method
        initial_current_player = self.game.current_player

        # Switch player and check if the current player has changed
        self.game.switch_player()
        self.assertNotEqual(initial_current_player, self.game.current_player)

        # Switch player again and check if it has reverted to the initial player
        self.game.switch_player()
        self.assertEqual(initial_current_player, self.game.current_player)

    
if __name__ == "__main__":
    unittest.main()