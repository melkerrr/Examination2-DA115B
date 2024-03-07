import unittest
from stats import Stats
from player import Player

class TestStats(unittest.TestCase):
    def test_initialization(self):
        # Test initialization of stats instance
        stats = Stats()
        self.assertEqual(stats.players, {})
        self.assertEqual(stats.total_games_played, 0)
        self.assertEqual(stats.total_wins, 0)
        self.assertEqual(stats.total_losses, 0)
        self.assertEqual(stats.total_draws, 0)

    def test_add_player(self):
        # Test add_players method
        stats = Stats()
        player = Player("Test Player")
        stats.add_player(player)
        self.assertEqual(
            stats.players, {"Test Player": {"score": 0, "games_played": 0}}
        )
        self.assertIn("Test Player", stats.players)

    def test_update_stats(self):
        # Test update_stats method
        stats = Stats()
        stats.players = {"Test Player": {"score": 50, "games_played": 1}}
        stats.update_stats("Test Player", 25)
        self.assertEqual(stats.players["Test Player"], {"score": 75, "games_played": 2})
        self.assertEqual(stats.total_games_played, 2)
        self.assertEqual(stats.total_wins, 1)
        self.assertEqual(stats.total_losses, 0)
        self.assertEqual(stats.total_draws, 0)

    def test_get_high_scores(self):
        # Test get_high_scores method
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
        self.assertEqual(len(high_scores), 3)

    def test_get_player_stats(self):
        # Test get_player_stats method
        stats = Stats()
        stats.players = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 75, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        player_stats = stats.get_player_stats("Player 2")
        expected_result = {"score": 75, "games_played": 2}
        self.assertEqual(player_stats, expected_result)

    def test_update_stats_invalid_player(self):
        # Test update_stats method with invalid player
        stats = Stats()
        stats.players = {"Test Player": {"score": 50, "games_played": 1}}
        stats.update_stats("Invalid Player", 25)
        self.assertNotIn("Invalid Player", stats.players)

    def test_no_high_scores(self):
        # Test getting high scores when no players exist
        stats = Stats()
        high_scores = stats.get_high_scores()
        self.assertEqual(high_scores, [])
        
    def test_no_player_stats(self):
        # Test getting stats for a player that doesn't exist
        stats = Stats()
        player_stats = stats.get_player_stats("Nonexistent Player")
        self.assertIsNone(player_stats)

    def test_update_invalid_stats(self):
        # Test updating stats with invalid input
        stats = Stats()
        stats.players = {"Test Player": {"score": 50, "games_played": 1}}
        stats.update_stats("Test Player", -25)
        self.assertEqual(stats.players["Test Player"], {"score": 50, "games_played": 1})

    def test_add_duplicate_player(self):
        # Test adding a duplicate player
        stats = Stats()
        player1 = Player("Player")
        player2 = Player("Player")
        stats.add_player(player1)
        stats.add_player(player2)
        self.assertEqual(len(stats.players), 1)

if __name__ == "__main__":
    unittest.main()
