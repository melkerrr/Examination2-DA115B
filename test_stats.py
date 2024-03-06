import unittest
from stats import Stats
from player import Player


class TestStats(unittest.TestCase):
    def test_initialization(self):
        # test initialization of stats instance
        stats = Stats()
        self.assertEqual(stats.players, {})

    def test_add_player(self):
        # Test add_players method
        stats = Stats()
        player = Player("Test Player")
        stats.add_player(player)
        self.assertEqual(
            stats.players, {"Test Player": {"score": 0, "games_played": 0}}
        )

    def test_update_stats(self):
        # test update_stats method
        stats = Stats()
        stats.players = {"Test Player": {"score": 50, "games_played": 1}}
        stats.update_stats("Test Player", 25)
        self.assertEqual(stats.players["Test Player"], {"score": 75, "games_played": 2})

    def test_get_high_scores(self):
        # test get_high_scores method
        stats = Stats()
        stats.players = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 75, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        high_scores = stats.get_high_scores()
        expected_result = [
            ("Player 3", {"score": 150, "games_played": 5}),
            ("Player 1", {"score": 100, "games_played": 3}),
            ("Player 2", {"score": 75, "games_played": 2}),
        ]
        self.assertEqual(high_scores, expected_result)


if __name__ == "__main__":
    unittest.main()
