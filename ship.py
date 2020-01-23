import pygame
# import settings


class Ship:
    """Class for Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # initial position of ship at mid bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for horizontal position of ship.
        self.x = float(self.rect.x)

        # Store decimal value for vertical position of ship.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        
    def blitme(self):
        """Draw one ship image over the other"""
        # draw ship at current location
        self.screen.blit(self.image, self.rect)


    def update(self):
        """Update ship's movement using the Movement Flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_horizontal_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_horizontal_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_vertical_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_vertical_speed

        # Update rect object from self x, y
        self.rect.x = self.x
        self.rect.y = self.y


    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)