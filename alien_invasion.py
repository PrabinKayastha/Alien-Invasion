import sys

import pygame
from pygame.locals import *


from settings import Settings
from ship import Ship



class AlienInvasion:
    '''Overall Class to manage game assets and behaviour.'''

    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

        # set background color
        self.bg_color = self.settings.bg_color

    def run_game(self):
        '''Start the main loop to run the game'''
        while True:
            # watch for keyboard and mouse events
            self._check_events()
            self.ship.update()
            self._update_screen()


    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move Right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Move Left
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    # Move Up
                    self.ship.moving_up = True
                elif event.key == pygame.K_DOWN:
                    # Move Down
                    self.ship.moving_down = True
             
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    # Move Right
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    # Move Left
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    # Move Up
                    self.ship.moving_up = False
                elif event.key == pygame.K_DOWN:
                    # Move Down
                    self.ship.moving_down = False
                


    def _update_screen(self):
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()



if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()