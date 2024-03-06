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

    @patch("builtins.input", side_effects=["h"])
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
        self.assertEqual(
            player.score, 3
        )  # Player should earn 3 points despite invalid input


if __name__ == "__main__":
    unittest.main()
