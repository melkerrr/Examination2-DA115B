import unittest
from difficulty import Difficulty


class TestDifficulty(unittest.TestCase):
    def test_easy_difficulty(self):
        # Test decide_roll_again method for easy difficulty
        difficulty = Difficulty("easy")
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Always rolls again in easy mode
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in easy mode

    def test_hard_difficulty(self):
        # Test decide_roll_again method for hard difficulty
        difficulty = Difficulty("hard")
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Rolls again with low points
        self.assertTrue(difficulty.decide_roll_again(20, 50))  # Doesn't roll again with high points
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in hard mode

    def test_default_difficulty(self):
        # Test decide_roll_again method for default difficulty
        difficulty = Difficulty("medium")  # Setting an unrecognized difficulty level
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Should return True by default
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in default mode

    def test_invalid_difficulty(self):
        # Test decide_roll_again method for invalid difficulty
        difficulty = Difficulty("invalid")  # Setting an invalid difficulty level
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Should return True for any points with invalid mode
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in invalid mode

    def test_boundary_conditions(self):
        # Test boundary conditions for hard difficulty
        difficulty = Difficulty("hard")
        self.assertTrue(difficulty.decide_roll_again(14, 65))  # Rolls again with points slightly below threshold
        self.assertTrue(difficulty.decide_roll_again(15, 65))  # Doesn't roll again with points exactly at threshold
        self.assertTrue(difficulty.decide_roll_again(14, 66))  # Rolls again with score slightly below threshold
        self.assertTrue(difficulty.decide_roll_again(14, 64))  # Rolls again with score slightly below threshold
        self.assertTrue(difficulty.decide_roll_again(14, 80))  # Rolls again with total score slightly below limit
        self.assertFalse(difficulty.decide_roll_again(15, 80))  # Doesn't roll again with points exactly at threshold

    def test_default_behavior(self):
        # Test default behavior when difficulty is not specified
        difficulty = Difficulty()  # Using default difficulty
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Should return True by default
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in default mode

    def test_easy_boundary_conditions(self):
        # Test boundary conditions for easy difficulty
        difficulty = Difficulty("easy")
        self.assertTrue(difficulty.decide_roll_again(1, 50))  # Always rolls again with any points in easy mode
        self.assertTrue(difficulty.decide_roll_again(0, 50))  # Always rolls again with any points in easy mode

    def test_hard_boundary_conditions(self):
        # Test boundary conditions for hard difficulty
        difficulty = Difficulty("hard")
        self.assertTrue(difficulty.decide_roll_again(14, 79))  # Rolls again with total score slightly below limit
        self.assertTrue(difficulty.decide_roll_again(14, 80))  # Doesn't roll again with total score at limit
        self.assertFalse(difficulty.decide_roll_again(15, 79))  # Doesn't roll again with points exactly at threshold

    def test_unrecognized_difficulty(self):
        # Test decide_roll_again method for unrecognized difficulty
        difficulty = Difficulty("unknown")
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Should return True for any points with unrecognized mode
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points in unrecognized mode

    def test_no_difficulty_specified(self):
        # Test behavior when no difficulty is specified
        difficulty = Difficulty(None)
        self.assertTrue(difficulty.decide_roll_again(10, 50))  # Should return True when no difficulty is specified
        self.assertTrue(difficulty.decide_roll_again(0, 0))  # Always rolls again with any points when no difficulty is specified

if __name__ == "__main__":
    unittest.main()
