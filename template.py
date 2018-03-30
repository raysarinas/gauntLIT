# Name of Game
# Summary of game.

import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():

   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (500, 400) # example window size
   windowTitle = 'Title' # example title
   frameDelay = 0.02 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   center = [200, 200] # example - replace

   # Draw objects
   # The next line is an example - replace it
   pygame.draw.circle(surface, pygame.Color('green'), center, 50, 0)

   # Refresh the display
   pygame.display.update()

   # Loop forever
   while True:
      # Handle events
      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         # Handle additional events

      # Update and draw objects for the next frame
      gameOver = update(center, surface)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(center, surface):
   # Check if the game is over. If so, end the game and
   # returnTrue. Otherwise, update the game objects, draw
   # them, and return False.
   # This is an example update function - replace it.
   # - center is a list containing the x and y int coords
   # of the center of a circle
   # - surface is the pygame.Surface object for the window

   if False: # check if the game is over
      return True
   else: # continue the game
      for index in range(0, 2):
         center[index] = center[index] + 1
         pygame.draw.circle(surface, pygame.Color('green'), center, 50 , 0)
      return False

main()
