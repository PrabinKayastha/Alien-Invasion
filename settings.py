class Settings:
    """A class to store settings for Alien Invasion"""

    def __init__(self):
        """Initialize game settings"""

        """Screen settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        """Ship Settings"""
        self.ship_horizontal_speed = 1.5
        self.ship_vertical_speed = 1.5