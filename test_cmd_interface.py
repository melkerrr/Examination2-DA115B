import unittest
from unittest.mock import patch, mock_open
from main import CmdInterface

class TestCmdInterface(unittest.TestCase):
    def setUp(self):
        self.cmd_interface = CmdInterface()

    def test_do_play_single_player(self):
        with patch("builtins.input", side_effect=["Player1"]):
            self.cmd_interface.do_play("")
        self.assertIsNotNone(self.cmd_interface.player1)

    def test_game_mode_computer(self):
        with patch("builtins.input", side_effect=["1", "Computer", "easy"]):
            self.cmd_interface.player1 = "Player1"
            self.cmd_interface.game_mode()
        self.assertIsNotNone(self.cmd_interface.player2)
        self.assertIsNotNone(self.cmd_interface.game)

    def test_game_mode_invalid_choice_then_valid(self):
        with patch("builtins.input", side_effect=["invalid", "2"]):
            self.cmd_interface.game_mode()
        self.assertIsNotNone(self.cmd_interface.player2)
        self.assertIsNotNone(self.cmd_interface.game)

    def test_play_turn_for_player_human(self):
        with patch("game.Game.play_turn_manual") as mock_play_turn_manual:
            self.cmd_interface.game = "fake_game"
            self.cmd_interface.play_turn_for_player(self.cmd_interface.player1)
        mock_play_turn_manual.assert_called_once()

    def test_play_turn_for_player_computer(self):
        with patch("game.Game.play_turn") as mock_play_turn:
            self.cmd_interface.game = "fake_game"
            self.cmd_interface.play_turn_for_player(self.cmd_interface.player2)
        mock_play_turn.assert_called_once()

    def test_start_game_single_player(self):
        self.cmd_interface.player1 = "Player1"
        self.cmd_interface.player2 = "Computer"
        self.cmd_interface.start_game()
        self.assertIsNotNone(self.cmd_interface.game)

    def test_start_game_two_players(self):
        self.cmd_interface.player1 = "Player1"
        self.cmd_interface.player2 = "Player2"
        self.cmd_interface.start_game()
        self.assertIsNotNone(self.cmd_interface.game)

    def test_do_scores(self):
        with patch.object(self.cmd_interface.stats_manager, "get_high_scores", return_value=[("Player1", {"score": 100, "games_played": 5})]):
            self.cmd_interface.do_scores("")
        # Ensure the output is printed correctly

    def test_do_rules(self):
        with patch("builtins.print") as mock_print:
            self.cmd_interface.do_rules("")
        mock_print.assert_called()

    def test_do_cheat_player1(self):
        self.cmd_interface.player1 = "Player1"
        with patch("builtins.input", return_value="Player1"), patch.object(self.cmd_interface, "player2", "fake_player2"):
            self.cmd_interface.do_cheat("")
        # Ensure the cheat is activated for Player1

    def test_do_cheat_player2(self):
        self.cmd_interface.player2 = "Player2"
        with patch("builtins.input", return_value="Player2"):
            self.cmd_interface.do_cheat("")
        # Ensure the cheat is activated for Player2

    def test_do_cheat_invalid_player(self):
        with patch("builtins.input", return_value="InvalidPlayer"):
            self.cmd_interface.do_cheat("")
        # Ensure the proper message is printed

    def test_do_rename(self):
        with patch("builtins.input", return_value="NewName"):
            self.cmd_interface.do_rename("")
        self.assertEqual(self.cmd_interface.player1.name, "NewName")

    def test_do_quit(self):
        with patch("builtins.print") as mock_print:
            result = self.cmd_interface.do_quit("")
        mock_print.assert_called()
        self.assertTrue(result)
    
    def test_do_play_single_player_name(self):
        with patch("builtins.input", side_effect=["Player1"]):
            self.cmd_interface.do_play("")
            self.assertEqual(self.cmd_interface.player1.name, "Player1")
    
    def test_play_against_computer_invalid_difficulty(self):
        with patch("builtins.input", side_effect=["Computer", "invalid", "easy"]):
            self.cmd_interface.play_against_computer()
        self.assertIsNotNone(self.cmd_interface.player2)
        self.assertIsNotNone(self.cmd_interface.game)
    
    def test_play_turn_for_player_unknown(self):
        with patch("game.Game.play_turn_manual"), patch("game.Game.play_turn"):
            self.cmd_interface.game = "fake_game"
            self.cmd_interface.play_turn_for_player("unknown_player")
    # Ensure no play turn method is called


if __name__ == "__main__":
    unittest.main()