import unittest
from unittest.mock import patch
from human_player import HumanPlayer

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

    @patch("builtins.input", side_effect=["h", "r"])
    @patch("random.randint", side_effect=[3, 2])
    def test_play_turn_hold_then_roll(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player holds then rolls
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points after holding
        player.play_turn()
        self.assertEqual(player.score, 5)  # Player should earn 5 points after rolling again

    @patch("builtins.input", side_effect=["r", "h", "r"])
    @patch("random.randint", side_effect=[2, 3, 1])
    def test_play_turn_roll_hold_roll(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player rolls, holds, then rolls again
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 2)  # Player should earn 2 points after first roll
        player.play_turn()
        self.assertEqual(player.score, 2)  # Player's score should remain 2 after holding
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points after second roll

    @patch("builtins.input", side_effect=["r", "r", "r", "r", "r", "r", "h"])
    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6, 2])
    def test_play_turn_multiple_rolls_with_hold(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player rolls multiple times with a hold
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 21)  # Player should earn 21 points after holding

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
        self.assertEqual(player.score, 3)  # Player should earn 3 points after valid input

    @patch("builtins.input", side_effect=["r", "r", "h", "invalid", "r"])
    @patch("random.randint", side_effect=[1, 2, 3, 4, 5])
    def test_play_turn_invalid_input_then_valid(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player enters invalid input then valid input
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 3)  # Player should earn 3 points after valid input

    @patch("builtins.input", side_effect=["r", "r", "h", "h", "r", "invalid", "r"])
    @patch("random.randint", side_effect=[1, 2, 3, 4, 5, 6, 3])
    def test_play_turn_multiple_invalid_input_then_valid(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player enters multiple invalid inputs then valid input
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 6)  # Player should earn 6 points after valid input

    @patch("builtins.input", side_effect=["r"] * 101)
    @patch("random.randint", side_effect=[1] * 101)
    def test_play_turn_limit_exceeded(self, mock_roll_dice, mock_input):
        # Test play_turn method when the player exceeds the maximum number of rolls
        player = HumanPlayer("Test Player")
        player.score = 0
        player.play_turn()
        self.assertEqual(player.score, 100)  # Player should earn 100 points after 100 rolls

if __name__ == "__main__":
    unittest.main()
