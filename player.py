"""
Module containing the Player class representing a player in the Pig Dice Game.
"""

class Player:
    """
    Class representing a player in the Pig Dice Game.
    """

    def __init__(self, name):
        """
        Initialize a player with a name and a score of 0.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.score = 0

    @property
    def name(self):
        """
        Get the name of the player.

        Returns:
            str: The name of the player.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Set the name of the player.

        Args:
            new_name (str): The new name for the player.
        """
        self._name = new_name

    def reset_score(self):
        """
        Reset the player's score to 0.
        """
        self.score = 0

    def update_score(self, points):
        """
        Update the player's score by adding the given points.

        Args:
            points (int): The points to add to the player's score.
        """
        self.score += points
