class GameStats:
    """Track the statistics forAlien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive status.
        self.game_active = False

        # Highscore should never be reset and should be read from a txt file.
        with open("highscore.txt", 'r') as fr:
            try:
                self.high_score = int(fr.read())
            except ValueError as e:
                self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
