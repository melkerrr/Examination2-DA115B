import unittest
from unittest.mock import mock_open, patch
from statsmanager import StatsManager


class TestStatsManager(unittest.TestCase):
    def test_initialization(self):
        # Test initialization of StatsManager instance
        stats_manager = StatsManager()
        self.assertEqual(stats_manager.stats_file, "stats.json")
        self.assertEqual(stats_manager.stats, {})

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"Player 1": {"score": 100, "games_played": 3}}',
    )
    def test_load_stats(self, mock_open):
        # Test load_stats method
        stats_manager = StatsManager()
        stats_manager.load_stats()
        self.assertEqual(
            stats_manager.stats, {"Player 1": {"score": 100, "games_played": 3}}
        )
        mock_open.assert_called_once_with("stats.json", "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_stats(self, mock_open):
        # Test save_stats method
        stats_manager = StatsManager()
        stats_manager.stats = {"Player 1": {"score": 100, "games_played": 3}}
        stats_manager.save_stats()
        mock_open.assert_called_once_with("stats.json", "w")
        handle = mock_open()
        handle.write.assert_called_once_with(
            '{"Player 1": {"score": 100, "games_played": 3}}'
        )

    def test_update_stats(self):
        # Test update_stats method
        stats_manager = StatsManager()
        stats_manager.update_stats("Player 1", 50)
        self.assertEqual(
            stats_manager.stats, {"Player 1": {"score": 50, "games_played": 1}}
        )
        stats_manager.update_stats("Player 1", 25)
        self.assertEqual(
            stats_manager.stats, {"Player 1": {"score": 75, "games_played": 2}}
        )

    def test_get_high_scores(self):
        # Test get_high_scores method
        stats_manager = StatsManager()
        stats_manager.stats = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 75, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        high_scores = stats_manager.get_high_scores()
        expected_result = [
            ("Player 3", {"score": 150, "games_played": 5}),
            ("Player 1", {"score": 100, "games_played": 3}),
            ("Player 2", {"score": 75, "games_played": 2}),
        ]
        self.assertEqual(high_scores, expected_result)


if __name__ == "__main__":
    unittest.main()
