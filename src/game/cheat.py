"""
Module containing cheat functionalities.
"""

class Cheat:
    """
    A class representing cheat functionalities for a player.
    """

    @staticmethod
    def activate_cheat(player):
        """
        Activate cheat mode for the player, setting their score to 100.

        Args:
            player (Player): The player object to activate the cheat for.

        Returns:
            str: The name of the player whose cheat mode was activated.
        """
        player.score = 100
        return player.name

    def is_cheat_active(self):
        """
        Check if cheat mode is active for the player.

        Returns:
            bool: True if cheat mode is active, False otherwise.
        """
        # Implementation to check if cheat mode is active
        return False
