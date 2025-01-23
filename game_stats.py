class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Intialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Intialize statistics that can change during the game."""
        self.ships_limit = self.settings.ships_left