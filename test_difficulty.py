import unittest
from difficulty import Difficulty


class TestDifficulty(unittest.TestCase):
    def test_easy_difficulty(self):
        # Test decide_roll_again method for easy difficulty
        difficulty = Difficulty("easy")
        self.assertTrue(
            difficulty.decide_roll_again(10, 50)
        )  # Always rolls again in easy mode

    def test_hard_difficulty(self):
        # Test decide_roll_again method for hard difficulty
        difficulty = Difficulty("hard")
        self.assertTrue(
            difficulty.decide_roll_again(10, 50)
        )  # Rolls again if points < 15 and current_player_score + points < 80
        self.assertFalse(
            difficulty.decide_roll_again(20, 50)
        )  # Doesn't roll again if points >= 15 and current_player_score + points >= 80

    def test_default_difficulty(self):
        # Test decide_roll_again method for default difficulty
        difficulty = Difficulty("medium")  # Setting an unrecognized difficulty level
        self.assertTrue(
            difficulty.decide_roll_again(10, 50)
        )  # Should return True by default


if __name__ == "__main__":
    unittest.main()
