import unittest
from cheat import Cheat
from player import Player

class TestCheat(unittest.TestCase):
    def test_activate_cheat(self):
        # Test activating cheat for a player
        player = Player('Test Player')
        player.score = 50
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100) # Player's score should be set to 100
        self.assertEqual(player_name, 'Test Player') # The returned player name should match

    if __name__ == '__main__':
        unittest.main()