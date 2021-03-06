class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080
        # self.bg_color = (230, 230, 230)

        # Score
        self.score_Alien = 50

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1.0

        # Bullet alien setting
        self.alien_bullet_color = (50,36,25)

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Mothership
        self.mothership_speed = 1.0
