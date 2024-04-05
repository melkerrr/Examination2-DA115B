import unittest
from unittest.mock import patch
from main import CmdInterface
from player import Player
from human_player import HumanPlayer
from game import Game

class TestCmdInterface(unittest.TestCase):
    def setUp(self):
        self.cmd_interface = CmdInterface()

    @patch('builtins.input', side_effect=["1", "Computer", "easy"])
    @patch('main.CmdInterface.start_game', autospec=True)
    def test_game_mode_computer(self, mock_start_game, mock_input):
        self.cmd_interface.player1 = Player("Player1")
        self.cmd_interface.game_mode()
        self.assertIsInstance(self.cmd_interface.player2, Player)
        mock_start_game.assert_called_once()

    @patch('builtins.input', side_effect=["invalid", "2", "Player2", "quit"])
    @patch('main.CmdInterface.start_game', autospec=True)
    def test_game_mode_invalid_choice_then_valid(self, mock_start_game, mock_input):
        self.cmd_interface.player1 = Player("Player1")
        self.cmd_interface.game_mode()
        self.assertIsInstance(self.cmd_interface.player2, HumanPlayer)
        mock_start_game.assert_called_once()

    @patch('builtins.input', side_effect=['r', 'r', 'h'])
    @patch('game.Game.roll_dice', side_effect=[5, 5, 1])
    def test_play_turn_for_player_human(self, mock_roll_dice, mock_input):
        self.cmd_interface.player1 = Player("Player1")
        self.cmd_interface.player2 = HumanPlayer("Player2")
        self.cmd_interface.game = Game(self.cmd_interface.player1, self.cmd_interface.player2)
        self.cmd_interface.play_turn_for_player(self.cmd_interface.player1)

    @patch('builtins.input', side_effect=['r', 'h'])
    @patch('game.Game.roll_dice', side_effect=[2, 2])
    def test_play_turn_for_player_computer(self, mock_roll_dice, mock_input):
        self.cmd_interface.player1 = Player("Player1")
        self.cmd_interface.player2 = Player("Computer")
        self.cmd_interface.game = Game(self.cmd_interface.player1, self.cmd_interface.player2)
        self.cmd_interface.play_turn_for_player(self.cmd_interface.player2)

    @patch('builtins.print')
    def test_do_scores(self, mock_print):
        self.cmd_interface.do_scores("")
        mock_print.assert_called()

    @patch('builtins.print')
    def test_do_rules(self, mock_print):
        self.cmd_interface.do_rules("")
        mock_print.assert_called()

    @patch('builtins.input', return_value="Player1")
    @patch('builtins.print')
    def test_do_cheat_player1(self, mock_print, mock_input):
        self.cmd_interface.player1 = Player("Player1")
        self.cmd_interface.do_cheat("")
        self.assertEqual(self.cmd_interface.player1.score, 100)

    @patch('builtins.input', return_value="NewName")
    @patch('builtins.print')
    def test_do_rename(self, mock_print, mock_input):
        self.cmd_interface.player1 = Player("OldName")
        self.cmd_interface.do_rename("")
        self.assertEqual(self.cmd_interface.player1.name, "NewName")


if __name__ == "__main__":
    unittest.main()