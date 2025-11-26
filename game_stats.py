import os

class GameStats:
    def __init__(self):
        self.score = 0
        self.high_score_file = "high_score.txt"
        self.high_score = self.load_high_score()

    def load_high_score(self):
        if os.path.exists(self.high_score_file):
            try:
                with open(self.high_score_file, 'r') as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0

    def save_high_score(self):
        with open(self.high_score_file, 'w') as f:
            f.write(str(self.high_score))
