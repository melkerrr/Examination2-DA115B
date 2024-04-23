import unittest
from cheat import Cheat
from player import Player


class TestCheat(unittest.TestCase):
    def test_activate_cheat(self):
        # Test activating cheat for a player
        player = Player("Test Player")
        player.score = 50
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Test Player"
        )  # The returned player name should match

    def test_activate_cheat_with_zero_score(self):
        # Test activating cheat for a player with zero initial score
        player = Player("Zero Player")
        player.score = 0
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Zero Player"
        )  # The returned player name should match

    def test_activate_cheat_with_negative_score(self):
        # Test activating cheat for a player with a negative initial score
        player = Player("Negative Player")
        player.score = -20
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Negative Player"
        )  # The returned player name should match

    def test_activate_cheat_multiple_times(self):
        # Test activating cheat for a player multiple times
        player = Player("Multi Player")
        player.score = 30
        Cheat.activate_cheat(player)
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Multi Player"
        )  # The returned player name should match

    def test_activate_cheat_no_player_name(self):
        # Test activating cheat for a player without a name
        player = Player(name=" ")
        player.score = 70
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, " "
        )  # The returned player name should be an empty string

    def test_activate_cheat_on_different_players(self):
        # Test activating cheat for different players
        player1 = Player("Player One")
        player1.score = 80
        player2 = Player("Player Two")
        player2.score = 90

        Cheat.activate_cheat(player1)
        Cheat.activate_cheat(player2)

        self.assertEqual(player1.score, 100)  # Player One's score should be set to 100
        self.assertEqual(player2.score, 100)  # Player Two's score should be set to 100

    def test_activate_cheat_with_high_initial_score(self):
        # Test activating cheat for a player with a high initial score
        player = Player("High Scorer")
        player.score = 150
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "High Scorer"
        )  # The returned player name should match

    def test_activate_cheat_with_decimal_score(self):
        # Test activating cheat for a player with a decimal initial score
        player = Player("Decimal Player")
        player.score = 30.5
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Decimal Player"
        )  # The returned player name should match

    def test_activate_cheat_with_string_score(self):
        # Test activating cheat for a player with a string initial score
        player = Player("String Player")
        player.score = "50"
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "String Player"
        )  # The returned player name should match

    def test_activate_cheat_with_missing_score(self):
        # Test activating cheat for a player with missing or undefined initial score
        player = Player("Missing Score Player")
        player_name = Cheat.activate_cheat(player)
        self.assertEqual(player.score, 100)  # Player's score should be set to 100
        self.assertEqual(
            player_name, "Missing Score Player"
        )  # The returned player name should match


if __name__ == "__main__":
    unittest.main()
