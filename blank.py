import pygame, sys, time
from pygame.locals import *

# User-defined classes

# User-defined functions

def main():
   # Initialize pygame
   pygame.init()

   # Set window size and title, and frame delay
   surfaceSize = (800, 600)
   windowTitle = 'Pong'
   frameDelay = 0.01 # smaller is faster game

   # Create the window
   surface = pygame.display.set_mode(surfaceSize, 0, 0)
   pygame.display.set_caption(windowTitle)

   # create and initialize objects
   gameOver = False
   fgColor = pygame.Color('white')
   bgColor = pygame.Color('black')
   center = [surfaceSize[0] // 2, surfaceSize[1] // 2]
   radius = 5
   speed = [4, 1]
   pWidth = 10
   pHeight = 40
   pXOffset = 100
   pYOffset = (surfaceSize[1] - pHeight) // 2
   pLeft = pygame.Rect(pXOffset, pYOffset, pWidth, pHeight)
   pRight = pygame.Rect(surfaceSize[0] - pXOffset - pWidth, pYOffset, pWidth, pHeight)

   # Draw objects
   pygame.draw.circle(surface, fgColor, center, radius)
   pygame.draw.rect(surface, fgColor, pLeft)
   pygame.draw.rect(surface, fgColor, pRight)

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

      # Update and draw objects for next frame
      gameOver = update(fgColor, bgColor, center, radius, speed, pLeft, pRight, surface)

      # Refresh the display
      pygame.display.update()

      # Set the frame speed by pausing between frames
      time.sleep(frameDelay)

def update(fgColor, bgColor, center, radius, speed, pLeft, pRight, surface):
   # Check if the game is over. If so, end the game and
   # return True. Otherwise, update the game objects, draw
   # them, and return False.
   # - fgColor is the pygame.Color of the ball and paddles
   # - bgColor is the background color used to erase
   # - center is a list containing the x and y int coords
   # of the center of the ball
   # - radius is the int pixel radius of the ball
   # - speed is a list containing the x and y components
   #   of the dot speed in pixels per frame
   # - paddleColor is the pygame.Color of the paddles
   # - pLeft is a pygame.Rect that represents the left player's paddle
   # - pRight is a pygame.Rect that represents the right player's paddle
   # - surface is the window's pygame.Surface object

   if False :
      return True
   else:
      surface.fill(bgColor)
      moveBall(center, radius, speed, pLeft, pRight, surface)
      pygame.draw.circle(surface, fgColor, center, radius)
      pygame.draw.rect(surface, fgColor, pLeft)
      pygame.draw.rect(surface, fgColor, pRight)
      return False

def moveBall(center, radius, speed, pLeft, pRight, surface):
   # Change the location and the speed of the ball so it
   # remains on the surface by bouncing from the top or
   # bottom edges or the paddles and increments the score and
   # respawns if it hits the left or right edge
   # - center is a list containing the x and y int coords
   # of the center of the ball
   # - radius is the int pixel radius of the ball
   # - speed is a list containing the x and y components
   #   of the ball speed in pixels per frame
   # - pLeft is the left paddle
   # - pRight is the right paddle
   # - surface is the window's pygame.Surface object

   size = surface.get_size()
   for coord in range(0, 2):
      # move ball
      center[coord] = center[coord] + speed[coord]
      # check left or top collisions
      if center[coord] < radius:
         speed[coord] = - speed[coord]
      # check right or bottom collisions
      if center[coord] + radius > size[coord]:
         speed[coord] = - speed[coord]

   # check paddle collisions
   if pRight.collidepoint(center) and speed[0] > 0 :
      speed[0] = -speed[0]
   if pLeft.collidepoint(center) and speed[0] < 0 :
      speed[0] = -speed[0]

main()
