import json


class StatsManager:
    def __init__(self):
        self.stats_file = "stats.json"
        self.stats = self.load_stats()

    def load_stats(self):
        try:
            with open(self.stats_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_stats(self):
        with open(self.stats_file, "w") as file:
            json.dump(self.stats, file)

    def update_stats(self, player_name, score):
        if player_name not in self.stats:
            self.stats[player_name] = {"score": score, "games_played": 1}
        else:
            self.stats[player_name]["score"] += score
            self.stats[player_name]["games_played"] += 1
        self.save_stats()

    def get_high_scores(self):
        return sorted(self.stats.items(), key=lambda x: x[1]["score"], reverse=True)
