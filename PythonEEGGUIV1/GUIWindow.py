import sys
import pygame
from Settings import Settings

class GUIWindow:
    # overall class that manages the gui
    
    def __init__(self):
        # initialize the game and create resources
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screenWidth,self.settings.screenHeight)) #sets the screen width and height
        pygame.display.set_caption("Python GUI V1") #sets the application title
        
    def run_program(self):
        # start of the main loop
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            #redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bgColor)
                    
            # make the most recently drawn screen visible
            pygame.display.flip()