import unittest
from unittest.mock import patch
from io import StringIO
from main import CmdInterface

class TestCmdInterface(unittest.TestCase):
    def setUp(self):
        self.cmd_interface = CmdInterface()

    def tearDown(self):
        # Reset the state after each test
        self.cmd_interface = None

    @patch("builtins.input", side_effect=["1", "1", "easy", "no"])
    def test_play_against_computer(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_against_computer()

        self.assertEqual(self.cmd_interface.player2.name, "Computer")
        self.assertIn("Choose difficulty level (easy/hard): ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["2", "Player 2", "no"])
    def test_play_as_two_players(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_as_two_players()

        self.assertEqual(self.cmd_interface.player2.name, "Player 2")
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["1", "2", "easy", "no"])
    def test_start_game(self, mock_input):
        self.cmd_interface.player1 = "Player 1"
        self.cmd_interface.player2 = "Player 2"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.start_game()

        self.assertIsNotNone(self.cmd_interface.game)
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["yes", "no"])
    def test_do_quit(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.do_quit("")

        self.assertEqual(fake_output.getvalue().strip(), "See you soon!")
        self.assertTrue(self.cmd_interface.game_over)

    @patch("builtins.input", side_effect=["2", "Player 2", "no"])
    def test_play_as_two_players_name(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_as_two_players()

        self.assertIn("Enter name for Player 1: ", fake_output.getvalue())
        self.assertIn("Enter name for Player 2: ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["1", "1", "easy", "no"])
    def test_play_against_computer_difficulty(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_against_computer()

        self.assertIn("Choose difficulty level (easy/hard): ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["1", "1", "easy", "no"])
    def test_play_against_computer_start_game(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_against_computer()

        self.assertIn("The game has started!", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["1", "1", "easy", "no"])
    def test_play_against_computer_game_over(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.play_against_computer()

        self.assertIn("Game Over!", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_over)

    @patch("builtins.input", side_effect=["1", "2", "easy", "no"])
    def test_start_game_players_assigned(self, mock_input):
        self.cmd_interface.player1 = "Player 1"
        self.cmd_interface.player2 = "Player 2"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.start_game()

        self.assertEqual(self.cmd_interface.game.player1, "Player 1")
        self.assertEqual(self.cmd_interface.game.player2, "Player 2")
        self.assertTrue(self.cmd_interface.game_started)
    
    @patch("builtins.input", side_effect=["1", "2", "easy", "no"])
    def test_start_game_game_over(self):
        self.cmd_interface.player1 = "Player 1"
        self.cmd_interface.player2 = "Player 2"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.start_game()

        self.assertIn("Game Over!", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_over)
    @patch("builtins.input", side_effect=["1", "1", "easy", "no"])
    def test_do_play_play_against_computer(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.do_play("")

        # Ensure player1 is set
        self.assertIsNotNone(self.cmd_interface.player1)
        self.assertEqual(self.cmd_interface.player1.name, "Player 1")

        # Ensure game mode is chosen
        self.assertIn("Choose game mode", fake_output.getvalue())

        # Choose to play against the computer
        self.assertIn("1. Play against computer", fake_output.getvalue())
        self.assertIn("Enter your choice: ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

        # Check that play_against_computer is called
        self.assertIsNotNone(self.cmd_interface.player2)
        self.assertEqual(self.cmd_interface.player2.name, "Computer")
        self.assertIn("Choose difficulty level (easy/hard): ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

    @patch("builtins.input", side_effect=["2", "Player 2", "no"])
    def test_do_play_play_as_two_players(self, mock_input):
        with patch("sys.stdout", new=StringIO()) as fake_output:
            self.cmd_interface.do_play("")

        # Ensure player1 is set
        self.assertIsNotNone(self.cmd_interface.player1)
        self.assertEqual(self.cmd_interface.player1.name, "Player 1")

        # Ensure game mode is chosen
        self.assertIn("Choose game mode", fake_output.getvalue())

        # Choose to play as two players
        self.assertIn("2. Play as 2 players", fake_output.getvalue())
        self.assertIn("Enter your choice: ", fake_output.getvalue())
        self.assertTrue(self.cmd_interface.game_started)

        # Check that play_as_two_players is called
        self.assertIsNotNone(self.cmd_interface.player2)
        self.assertEqual(self.cmd_interface.player2.name, "Player 2")
        self.assertTrue(self.cmd_interface.game_started)

    

if __name__ == "__main__":
    unittest.main()
