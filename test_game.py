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

if __name__ == "__main__":
    unittest.main()
