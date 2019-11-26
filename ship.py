import pygame


class Ship:
    """Class for Ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
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
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        elif self.moving_up:
            self.rect.y -= 1
        elif self.moving_down:
            self.rect.y += 1