"""
Module containing the Stats class representing player statistics.
"""

class Stats:
    """
    Class representing player statistics.
    """

    def __init__(self):
        """
        Initialize the Stats object with an empty dictionary of players.
        """
        self.players = {}

    def add_player(self, player):
        """
        Add a player to the statistics.

        Args:
            player (Player): The player to add.
        """
        self.players[player.name] = {"score": player.score, "games_played": 0}

    def update_stats(self, player_name, score):
        """
        Update the statistics for a player with the given score.

        Args:
            player_name (str): The name of the player.
            score (int): The score to update for the player.
        """
        if player_name in self.players:
            self.players[player_name]["score"] += score
            self.players[player_name]["games_played"] += 1

    def get_high_scores(self):
        """
        Get the high scores, sorted by score in descending order.

        Returns:
            list: A list of tuples containing player names and their corresponding statistics.
        """
        return sorted(self.players.items(), key=lambda x: x[1]["score"], reverse=True)
    