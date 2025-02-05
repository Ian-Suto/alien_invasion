from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Intialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # High score  should never be reset.
        self.high_score = int(self.read_highest_score())

    def reset_stats(self):
        """Intialize statistics that can change during the game."""
        self.ships_limit = self.settings.ships_left
        self.score = 0
        self.level = 1

    def read_highest_score(self):
        """Read the highest score from textfile."""
        path = Path('text_file/highest_score.txt')
        contents = path.read_text()
        return contents