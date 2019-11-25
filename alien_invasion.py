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
        self.settngs = Settings()

        self.screen = pygame.display.set_mode((self.settngs.screen_width, self.settngs.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

        # set background color
        self.bg_color = (255, 255, 255)

    def run_game(self):
        '''Start the main loop to run the game'''
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            self.screen.fill(self.settngs.bg_color)
            self.ship.blitme()

            
            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()