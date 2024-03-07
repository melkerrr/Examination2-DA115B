"""
statsmanager.py: A module for managing player statistics.
"""

import json

class StatsManager:
    """
    A class to manage player statistics.
    """

    def __init__(self):
        """
        Initializes the StatsManager with a stats file and loads existing statistics.
        """
        self.stats_file = "stats.json"
        self.stats = self.load_stats()

    def load_stats(self):
        """
        Loads statistics from the stats file.
        """
        try:
            with open(self.stats_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_stats(self):
        """
        Saves statistics to the stats file.
        """
        with open(self.stats_file, "w", encoding="utf-8") as file:
            json.dump(self.stats, file)

    def update_stats(self, player_name, score):
        """
        Updates player statistics with the given score.
        """
        if player_name not in self.stats:
            self.stats[player_name] = {"score": score, "games_played": 1}
        else:
            self.stats[player_name]["score"] += score
            self.stats[player_name]["games_played"] += 1
        self.save_stats()

    def get_high_scores(self):
        """
        Returns the high scores sorted by score.
        """
        return sorted(self.stats.items(), key=lambda x: x[1]["score"], reverse=True)


if __name__ == "__main__":
    manager = StatsManager()
    manager.update_stats("Player1", 100)
    manager.update_stats("Player2", 150)
    high_scores = manager.get_high_scores()
    print(high_scores)
