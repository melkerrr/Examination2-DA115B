class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def reset_score(self):
        self.score = 0

    def update_score(self, points):
        self.score += points
