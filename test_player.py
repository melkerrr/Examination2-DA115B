import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def test_initialization(self):
        # Test initialization of Player instance
        player = Player("Test Player")
        self.assertEqual(player.name, "Test Player")
        self.assertEqual(player.score, 0)

    def test_name_property(self):
        # test name property
        player = Player("Test Player")
        self.assertEqual(player.name, "Test Player")

        # Test name setter
        player.name = "New name"
        self.assertEqual(player.name, "New name")

    def test_reset_score(self):
        # test reset_score method
        player = Player("Test Player")
        player.score = 100
        player.reset_score()
        self.assertEqual(player.score, 0)

    def test_update_score(self):
        # test update_score method
        player = Player("Test Player")
        player.update_score(50)
        self.assertEqual(player.score, 50)
        player.update_score(25)
        self.assertEqual(player.score, 75)


if __name__ == "__main__":
    unittest.main()
