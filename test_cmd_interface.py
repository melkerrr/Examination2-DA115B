import unittest
from unittest.mock import patch
from io import StringIO
from main import CmdInterface


class TestCmdInterface(unittest.TestCase):
    def setUp(self):
        self.cmdinterface = CmdInterface()

    @patch("builtins.input", sideeffect=["1", "1", "easy", "no"])
    def testplay_against_computer(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_against_computer()
        self.assertEqual(self.cmd_interface.player2.name, "Computer")
        self.assertIn("Choose difficulty level (easy/hard): ", fake_output.getvalue())

    @patch("builtins.input", side_effect=["2", "Player 2", "no"])
    def test_play_as_two_players(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_as_two_players()
        self.assertEqual(self.cmd_interface.player2.name, "Player 2")

    @patch("builtins.input", side_effect=["1", "2", "easy", "no"])
    def test_start_game(self, mock_input):
        self.cmd_interface.player1 = "Player 1"
        self.cmd_interface.player2 = "Player 2"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.start_game()
        self.assertIsNotNone(self.cmd_interface.game)

    @patch("builtins.input", side_effect=["yes", "no"])
    def test_do_quit(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.do_quit("")
        self.assertEqual(fake_output.getvalue().strip(), "See you soon!")


if __name__ == "__main__":
    unittest.main()
