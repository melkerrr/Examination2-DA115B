class Stats:
    def __init__(self):
        self.players = {}

    def add_player(self, player):
        self.players[player.name] = {'score': player.score, 'games_played': 0}

    def update_stats(self, player_name, score):
        self.players[player_name]['score'] += score
        self.players[player_name]['games_played'] += 1

    def get_high_scores(self):
        return sorted(self.players.items(), key=lambda x: x[1]['score'], reverse=True)