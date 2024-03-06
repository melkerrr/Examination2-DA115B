import unittest
from unittest.mock import patch
from game import Game
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player('Player 1')
        self.player2 = Player('Player 2')
        self.game = Game(self.player1, self.player2)

    @patch('builtins.input', side_effect=['r', 'h'])
    @patch('random.randint', return_value=3)
    def test_play_turn_player1(self, mock_roll_dice, mock_input):
        # Test play_turn method for player 1
        self.player1.score = 0
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 3) # Player 1 should earn 3 points

    @patch('builtins.input', side_effect=['r', 'h'])
    @patch('random.randint', return_value=1)
    def test_play_turn_player1_rolled_1(self, mock_roll_dice, mock_input):
        # Test play_turn method when player 1 rolls a 1
        self.player1.score = 0
        self.player2.score = 0
        self.game.play_turn()
        self.assertEqual(self.player1.score, 0) # Player 1's score should remain 0

        # Add more test methods...

if __name__ == '__main__':
    unittest.main()