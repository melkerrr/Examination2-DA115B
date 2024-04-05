import unittest 
from unittest.mock import patch
from human_player import HumanPlayer
from unittest import TestCase, mock

class TestHumanPlayer(unittest.TestCase):
    @patch("builtins.input", side_effect=["r", "h"])
    @patch("random.randint", return_value=3)
    def test_play_turn_roll(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player chooses to roll
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points

    @patch("builtins.input", side_effect=["h"])
    def test_play_turn_hold(self, mock_input):
        # Test play_turn method when the player chooses to hold
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 0)  # Player's score should remain 0

    @patch("builtins.input", side_effect=["invalid", "r", "h"])
    @patch("random.randint", return_value=3)
    def test_play_turn_invalid_choice(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player enters an invalid choice
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points despite invalid input

    @patch("builtins.input", side_effect=["r", "r", "h"])
    @patch("random.randint", side_effect=[4, 5, 3])
    def test_play_turn_multiple_rolls(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player rolls multiple times
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 9)  # Player should earn 9 points after multiple rolls

    @patch("builtins.input", side_effect=["h", "h"])
    def test_play_turn_hold_twice(self, mock_input):
        # Test play_turn method when the player holds twice in a row
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 0)  # Player's score should remain 0 after first hold
        player.play_turn()
        self.assertEqual(player.score, 0)  # Player's score should remain 0 after second hold

    @patch("builtins.input", side_effect=["", "r", "h"])
    @patch("random.randint", return_value=3)
    def test_play_turn_empty_input_then_valid(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player enters empty input then valid input
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points after valid inputF

if __name__ == "__main__":
    unittest.main()
