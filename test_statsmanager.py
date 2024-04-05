import unittest
from unittest.mock import mock_open, patch
from statsmanager import StatsManager

class TestStatsManager(unittest.TestCase):
    def test_save_stats_no_stats(self):
        stats_manager = StatsManager()
        stats_manager.save_stats()
        handle = mock_open()
        

    def test_save_stats_empty_stats(self):
        stats_manager = StatsManager()
        stats_manager.stats = {}
        stats_manager.save_stats()
        handle = mock_open()


    def test_save_stats_multiple_players(self):
        stats_manager = StatsManager()
        stats_manager.stats = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 75, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        stats_manager.save_stats()
        handle = mock_open()

    def test_get_high_scores_tiebreaker(self):
        stats_manager = StatsManager()
        stats_manager.stats = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 100, "games_played": 3},
            "Player 3": {"score": 90, "games_played": 5},
        }
        high_scores = stats_manager.get_high_scores()
        expected_result = [
            ("Player 1", {"score": 100, "games_played": 3}),
            ("Player 2", {"score": 100, "games_played": 3}),
            ("Player 3", {"score": 90, "games_played": 5}),
        ]
        self.assertEqual(high_scores, expected_result)
    

    def test_get_high_scores_tied_scores(self):
        stats_manager = StatsManager()
        stats_manager.stats = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 100, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        high_scores = stats_manager.get_high_scores()
        # Ensure that when scores are tied, the sorting considers the number of games played
        expected_result = [
            ("Player 3", {"score": 150, "games_played": 5}),
            ("Player 1", {"score": 100, "games_played": 3}),
            ("Player 2", {"score": 100, "games_played": 2}),
        ]
        self.assertEqual(high_scores, expected_result)


if __name__ == "__main__":
    unittest.main()
