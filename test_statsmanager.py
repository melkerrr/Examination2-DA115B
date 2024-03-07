import unittest
from unittest.mock import mock_open, patch
from statsmanager import StatsManager

class TestStatsManager(unittest.TestCase):
    def test_initialization(self):
        stats_manager = StatsManager()
        self.assertEqual(stats_manager.stats_file, "stats.json")
        self.assertEqual(stats_manager.stats, {})

    @patch("builtins.open", new_callable=mock_open, read_data='{"Player 1": {"score": 100, "games_played": 3}}')
    def test_load_stats(self, mock_open):
        stats_manager = StatsManager()
        stats_manager.load_stats()
        self.assertEqual(stats_manager.stats, {"Player 1": {"score": 100, "games_played": 3}})
        mock_open.assert_called_once_with("stats.json", "r")

    @patch("builtins.open", new_callable=mock_open)
    def test_save_stats(self, mock_open):
        stats_manager = StatsManager()
        stats_manager.stats = {"Player 1": {"score": 100, "games_played": 3}}
        stats_manager.save_stats()
        mock_open.assert_called_once_with("stats.json", "w")
        handle = mock_open()
        handle.write.assert_called_once_with('{"Player 1": {"score": 100, "games_played": 3}}')

    def test_update_stats(self):
        stats_manager = StatsManager()
        stats_manager.update_stats("Player 1", 50)
        self.assertEqual(stats_manager.stats, {"Player 1": {"score": 50, "games_played": 1}})
        stats_manager.update_stats("Player 1", 25)
        self.assertEqual(stats_manager.stats, {"Player 1": {"score": 75, "games_played": 2}})

    def test_get_high_scores(self):
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

    def test_load_stats_missing_file(self):
        stats_manager = StatsManager()
        stats_manager.load_stats()
        self.assertEqual(stats_manager.stats, {})

    def test_save_stats_no_stats(self):
        stats_manager = StatsManager()
        stats_manager.save_stats()
        handle = mock_open()
        handle.write.assert_not_called()

    def test_save_stats_empty_stats(self):
        stats_manager = StatsManager()
        stats_manager.stats = {}
        stats_manager.save_stats()
        handle = mock_open()
        handle.write.assert_called_once_with("{}", "w")

    def test_update_stats_invalid_player(self):
        stats_manager = StatsManager()
        stats_manager.update_stats("Nonexistent Player", 50)
        self.assertEqual(stats_manager.stats, {})

    def test_get_high_scores_empty_stats(self):
        stats_manager = StatsManager()
        high_scores = stats_manager.get_high_scores()
        self.assertEqual(high_scores, [])

    def test_save_stats_multiple_players(self):
        stats_manager = StatsManager()
        stats_manager.stats = {
            "Player 1": {"score": 100, "games_played": 3},
            "Player 2": {"score": 75, "games_played": 2},
            "Player 3": {"score": 150, "games_played": 5},
        }
        stats_manager.save_stats()
        handle = mock_open()
        handle.write.assert_called_once_with(
            '{"Player 1": {"score": 100, "games_played": 3}, '
            '"Player 2": {"score": 75, "games_played": 2}, '
            '"Player 3": {"score": 150, "games_played": 5}}',
            "w",
        )

    def test_load_stats_invalid_data(self):
        with patch(
            "builtins.open", new_callable=mock_open, read_data="Invalid JSON Data"
        ):
            stats_manager = StatsManager()
            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

    def test_invalid_file_contents(self):
        with patch(
            "builtins.open", new_callable=mock_open, read_data='{"Invalid": "Data"}'
        ):
            stats_manager = StatsManager()
            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})

    @patch("builtins.open", new_callable=mock_open, read_data='{"Player 1": {"score": 100, "games_played": 3}}')
    def test_load_stats(self, mock_open):
        stats_manager = StatsManager()
        stats_manager.load_stats()
        self.assertEqual(stats_manager.stats, {"Player 1": {"score": 100, "games_played": 3}})
        mock_open.assert_called_once_with("stats.json", "r")

    def test_load_stats_invalid_json(self):
        with patch("builtins.open", new_callable=mock_open, read_data='{"Player 1": {"score": 100, "games_played": 3, "invalid_key": "invalid"}}'):
            stats_manager = StatsManager()
            stats_manager.load_stats()
            self.assertEqual(stats_manager.stats, {})  # Invalid JSON should not affect stats

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
    
    def test_save_stats_invalid_data(self):
        stats_manager = StatsManager()
        stats_manager.stats = {"Player 1": {"score": 100, "games_played": 3, "invalid_key": "invalid"}}
        with patch("builtins.open", new_callable=mock_open):
            stats_manager.save_stats()
        # Ensure that invalid data is not saved
        handle = mock_open()
        handle.write.assert_not_called()

    def test_update_stats_negative_score(self):
        stats_manager = StatsManager()
        stats_manager.stats = {"Player 1": {"score": 100, "games_played": 3}}
        stats_manager.update_stats("Player 1", -50)
        # Ensure that negative scores do not update the stats
        self.assertEqual(stats_manager.stats, {"Player 1": {"score": 100, "games_played": 3}})

    def test_load_stats_corrupted_file(self):
        with patch("builtins.open", new_callable=mock_open, read_data='corrupted_json_data'):
            stats_manager = StatsManager()
            stats_manager.load_stats()
            # Ensure that loading from a corrupted file results in an empty stats dictionary
            self.assertEqual(stats_manager.stats, {})

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

    def test_load_stats_file_not_found(self):
        stats_manager = StatsManager()
    
    # Simulate the stats file not being found
        with patch("builtins.open", side_effect=FileNotFoundError):
            stats_manager.load_stats()
    
    # Ensure that stats are initialized to an empty dictionary
        self.assertEqual(stats_manager.stats, {})



if __name__ == "__main__":
    unittest.main()
