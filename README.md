Green Mario's Haunted Bungalow Rescue

INSTRUCTIONS/DESCRIPTION FOR THE GAME:
To play the game the user must first select there difficulty that they would like to play. There are options such as easy, medium,
and hard. The aim of the game is to get Luigi to Peach without being caught by the ghost which is following the player throughout the
game.

INSTRUCTIONS TO SET UP THE GAME:
This game runs on Pygame so that program must be downloaded for the game to function. To run the game, be in the directory of the our assignment and type into the terminal "python3 main.py".

**NOTES**
- There were a few bugs that we were unable to fix in time. One bug included that during a collision between the player and a ghost, the ghost would not properly draw in the position in which it had collided with player, appearing as though the ghost had not yet collided with the player (even though it would have and we are aware that this is correct by printing the range of the coordinates of both the player and the ghost at the time of collision). A correction factor was added to fix this issue, though in some locations on the screen, such as a corner, the issue still persisted. Another bug was that when running the game on the VM, sometimes the ghost would stop moving and chasing the player. We don't know why this happens, since the game runs smoothly and without any issues on our Macbooks.
- Various code developed from class and previously developed in Assignment 1 was used in this assignment, much of which had been modified. 'graph.py' and 'binary_heap.py' completely untouched and unmodified, though our implementation of Dijkstra's algorithm and finding the least cost path from Assignment 1 was modified to fit the needs of our game's functionality. 

REFERENCES
- **PYGAME DOCUMENTATION**
https://www.pygame.org/docs/index.html

- SPRITES: https://piq.codeus.net/u/Revawolf
- https://stackoverflow.com/questions/27867073/how-to-put-an-image-onto-a-sprite-pygame
- http://www.mariouniverse.com/sprites/gba/smb3
- Collisions with the walls: https://www.youtube.com/watch?v=8IRyt7ft7zg&t=388s
- Peach and Green Mario collision: https://stackoverflow.com/questions/42081204/pygame-collision-not-working-pygame-sprite-collide-rect
- https://stackoverflow.com/questions/20025367/pygame-making-a-sprite-move-along-a-predetermined-path-at-a-constant-speed
- https://stackoverflow.com/questions/28645597/how-to-draw-a-transparent-image-in-pygame
- https://stackoverflow.com/questions/18826788/converting-an-image-to-a-rect
- Press space: https://stackoverflow.com/questions/20748326/pygame-waiting-the-user-to-keypress-a-key
- https://i.pinimg.com/originals/3f/ee/f2/3feef297db2e56baeacde08ae854819f.jpg
- TEXT CENTERING https://stackoverflow.com/questions/23982907/python-library-pygame-centering-text
- http://pixeljoint.com/pixelart/87261.htm
- http://johanvinet.tumblr.com/tagged/Extreme-Exorcism
