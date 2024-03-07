import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def test_initialization(self):
        # Test initialization of Player instance
        player = Player("Test Player")
        self.assertEqual(player.name, "Test Player")
        self.assertEqual(player.score, 0)

    def test_name_property(self):
        # Test name property
        player = Player("Test Player")
        self.assertEqual(player.name, "Test Player")

        # Test name setter
        player.name = "New name"
        self.assertEqual(player.name, "New name")

    def test_reset_score(self):
        # Test reset_score method
        player = Player("Test Player")
        player.score = 100
        player.reset_score()
        self.assertEqual(player.score, 0)

    def test_update_score(self):
        # Test update_score method
        player = Player("Test Player")
        player.update_score(50)
        self.assertEqual(player.score, 50)
        player.update_score(25)
        self.assertEqual(player.score, 75)

    def test_score_properties(self):
        # Test score properties
        player = Player("Test Player")
        player.update_score(50)
        self.assertGreater(player.score, 0)
        player.reset_score()
        self.assertEqual(player.score, 0)

    def test_name_properties(self):
        # Test name properties
        player = Player("Test Player")
        self.assertNotEqual(player.name, "")
        self.assertIsInstance(player.name, str)

    def test_invalid_score_input(self):
        # Test invalid score input
        player = Player("Test Player")
        player.update_score(-25)
        self.assertEqual(player.score, 0)

    def test_multiple_score_updates(self):
        # Test updating score multiple times
        player = Player("Test Player")
        player.update_score(10)
        player.update_score(20)
        player.update_score(30)
        self.assertEqual(player.score, 60)

    def test_reset_score_idempotent(self):
        # Test reset_score method idempotent behavior
        player = Player("Test Player")
        player.reset_score()
        player.reset_score()
        self.assertEqual(player.score, 0)

    def test_name_type(self):
        # Test name type
        player = Player("Test Player")
        self.assertIsInstance(player.name, str)

        # Test name is not None
        self.assertIsNotNone(player.name)

        # Test name length
        self.assertGreater(len(player.name), 0)

        # Test name starts with capital letter
        self.assertTrue(player.name[0].isupper())

        # Test name is alphanumeric
        self.assertTrue(player.name.isalnum())

        # Test name does not contain special characters
        self.assertFalse(any(c.isalnum() for c in player.name))

        # Test name is not empty
        self.assertNotEqual(len(player.name), 0)

if __name__ == "__main__":
    unittest.main()
