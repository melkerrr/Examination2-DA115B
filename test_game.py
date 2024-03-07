import unittest
from unittest.mock import patch
from game import Game
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.game = Game(self.player1, self.player2)

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=3)
    def test_play_turn_player1(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 1
        self.player1.score = 0
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 3)  # Player 1 should earn 3 points
        self.assertEqual(self.game.current_player, self.player2)  # Current player should switch to player 2

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=1)
    def test_play_turn_player1_rolled_1(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 1 rolls a 1
        self.player1.score = 0
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 0)  # Player 1's score should remain 0
        self.assertEqual(self.game.current_player, self.player2)  # Current player should switch to player 2

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=6)
    def test_play_turn_player1_wins(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 1 wins
        self.player1.score = 0
        self.player2.score = 20
        self.game.play_turn()
        self.assertEqual(self.player1.score, 6)  # Player 1 should earn 6 points
        self.assertEqual(self.game.current_player, self.player1)  # Current player should remain player 1

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=1)
    def test_play_turn_player2(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 2
        self.player1.score = 0
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 0)  # Player 2's score should remain 0
        self.assertEqual(self.game.current_player, self.player1)  # Current player should switch to player 1

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[2, 2, 4])
    def test_play_turn_player1_multiple_rolls(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 1 with multiple rolls
        self.player1.score = 0
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 4)  # Player 1 should earn 4 points
        self.assertEqual(self.game.current_player, self.player2)  # Current player should switch to player 2

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[2, 1, 4])
    def test_play_turn_player1_rolled_1_mid_game(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 1 when player 1 rolls a 1 mid-game
        self.player1.score = 0
        self.player2.score = 10
        self.game.play_turn()
        self.assertEqual(self.player1.score, 0)  # Player 1's score should remain 0
        self.assertEqual(self.game.current_player, self.player2)  # Current player should switch to player 2

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[3, 3, 5])
    def test_play_turn_player1_wins_multiple_rolls(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 1 winning with multiple rolls
        self.player1.score = 10
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 5)  # Player 1 should earn 5 points
        self.assertEqual(self.game.current_player, self.player1)  # Current player should remain player 1

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=1)
    def test_play_turn_player2_rolled_1(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 2 rolls a 1
        self.player1.score = 10
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 0)  # Player 2's score should remain 0
        self.assertEqual(self.game.current_player, self.player1)  # Current player should switch to player 1

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=2)
    def test_play_turn_player2_rolled_2(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 2 rolls a 2
        self.player1.score = 10
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 2)  # Player 2 should earn 2 points
        self.assertEqual(self.game.current_player, self.player1)  # Current player should switch to player 1

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[1, 2, 3])
    def test_play_turn_player2_wins(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 2 wins
        self.player1.score = 10
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 3)  # Player 2 should earn 3 points
        self.assertEqual(self.game.current_player, self.player2)  # Current player should remain player 2

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[3, 4, 5])
    def test_play_turn_tie(self, mock_roll_dice, mock_input):
        # Test play_turn method when it's a tie
        self.player1.score = 10
        self.player2.score = 10
        self.game.play_turn()
        self.assertEqual(self.player1.score, 13)  # Player 1 should earn 3 points
        self.assertEqual(self.player2.score, 10)  # Player 2's score should remain 10

    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", side_effect=[2, 2, 3])
    def test_play_turn_player2_wins_multiple_rolls(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 2 wins with multiple rolls
        self.player1.score = 10
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 3)  # Player 2 should earn 3 points
        self.assertEqual(self.game.current_player, self.player2)  # Current player should remain player 2

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[1, 2, 1])
    def test_play_turn_player2_loses_after_rolling_1(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 2 loses after rolling a 1
        self.player1.score = 10
        self.player2.score = 0
        self.game.current_player = self.player2
        self.game.play_turn()
        self.assertEqual(self.player2.score, 0)  # Player 2's score should remain 0
        self.assertEqual(self.game.current_player, self.player1)  # Current player should switch to player 1

    def test_play_turn_manual(self):
        # Test play_turn_manual method for both players
        with patch("builtins.input", side_effect=["r", "h"]):
            # Test for player 1
            self.game.play_turn_manual()
            self.assertTrue(self.player1.score in [0, 1, 2, 3, 4, 5, 6])

            # Test for player 2
            self.game.current_player = self.player2
            self.game.play_turn_manual()
            self.assertTrue(self.player2.score in [0, 1, 2, 3, 4, 5, 6])

    def test_play_turn_computer_roll_one(self):
        # Test play_turn method when the computer rolls a 1
        self.game.current_player = self.player2  # Set current player as the computer
        with patch("game.Game.roll_dice", return_value=1), patch("builtins.print") as mock_print:
            self.game.play_turn()
            mock_print.assert_called_with("\nThe computer rolled a 1. Turn ends.")

    def test_play_turn_computer_hold(self):
        # Test play_turn method when the computer decides to hold
        self.game.current_player = self.player2  # Set current player as the computer
        self.player1.score = 80
        self.player2.score = 0
        with patch("game.Game.roll_dice", side_effect=[4, 3, 2, 1]), patch("builtins.print") as mock_print:
            self.game.play_turn()
            mock_print.assert_called_with("\nThe computer holds. Points earned: 9")

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

    @patch("builtins.print")
    @patch.object(Player, "update_score")
    @patch("game.Game.play_turn", side_effect=[None, None])  # Mocking two turns
    def test_play_game(self, mock_play_turn, mock_update_score, mock_print):
        # Set scores to ensure the game runs
        self.player1.score = 90
        self.player2.score = 80

        # Play the game
        self.game.play_game()

        # Assertions
        mock_play_turn.assert_called_with()  # Ensure play_turn is called during the game
        mock_update_score.assert_called()  # Ensure update_score is called after playing a turn
        mock_print.assert_called_with("Game Over!")  # Ensure "Game Over!" is printed
        # Add more assertions based on your specific print statements in play_game

if __name__ == "__main__":
    unittest.main()