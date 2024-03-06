"""
Module containing Difficulty class representing the difficulty level of the game.
"""

class Difficulty:
    """
    Class representing the difficulty level of the game.
    """

    def __init__(self, level="easy"):
        """
        Initialize the Difficulty object with a specified level.

        Args:
            level (str): The difficulty level. Default is 'easy'.
        """
        self.level = level

    def decide_roll_again(self, points, current_player_score):
        """
        Decide whether to roll again based on the current game state.

        Args:
            points (int): The points earned in the current turn.
            current_player_score (int): The current player's total score.

        Returns:
            bool: True if the computer should roll again, False otherwise.
        """
        if self.level == "easy":
            # When difficulty set to easy the computer always rolls again
            return True
        # When difficulty set to hard the computer rolls again only if it is advantageous
        # e.g. if the current turn's points are less than 15 or the total score is below 80,
        # the computer rolls again
        if self.level == "hard":
            return points < 15 or current_player_score + points < 80
        # default behavior if difficulty level is not recognized
        return True

    def change_difficulty(self, new_difficulty):
        """
        Change the difficulty level.

        Args:
            new_difficulty (str): The new difficulty level to set.
        """
        self.level = new_difficulty
