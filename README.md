# gauntLIT
CMPUT 275 FINAL PROJECT (the last time zac tries it with bonus pain from omid)

- **READ THIS FOR ALGORITHM IMPLEMENTATION** - https://www.redblobgames.com/pathfinding/tower-defense/implementation.html

- **PYGAME DOCUMENTATION**
https://www.pygame.org/docs/index.html

- maybe this will help with drawing walls: https://stackoverflow.com/questions/24301702/walls-in-pygame

- THIS LOOKS REALLY GOOD BUT I HAVENT READ IT YET. IT INCLUDES STUFF ON PATH FINDING AND HONESTLY WE COULD PROBABLY JUST MAKE A DUPLICATE OF THIS GAME BUT LIKE MAKE IT ALL MARIO AND WHATEVER ELSE
- https://eli.thegreenplace.net/tag/pygame-tutorial

- SPRITES: https://piq.codeus.net/u/Revawolf
- https://stackoverflow.com/questions/27867073/how-to-put-an-image-onto-a-sprite-pygame
- http://www.mariouniverse.com/sprites/gba/smb3

- Collisions with the walls: https://www.youtube.com/watch?v=8IRyt7ft7zg&t=388s

-Peach and Mario collision: https://stackoverflow.com/questions/42081204/pygame-collision-not-working-pygame-sprite-collide-rect

## DONE BY TUESDAY
- [x] got stuff started
- [x] ~~drew temp rectangles? for characters???~~
- [x] platforms drawn (randomly generated or no? we could just have one level) ~~[use tic tac toe for reference. could use/generate a board with a 2D array? only issue would be super slow running time O(n^2) or something like that i think]~~
- [x] have player/keyboard movement working properly
- [x] make sure player cant go through walls/platforms ~~[pong for reference]~~

## TODO BY THE END OF THE WEEK/WEEKEND/TUESDAY
- [ ] txt file with screen coordinates that will act as vertices and edges [DONE BY FRIDAY]
- [ ] ~~**ALGORITHM IMPLEMENTATION (Breadth First Search / Dijkstra?)** [DONE BY FRIDAY]~~
- [x] endgame conditions (i.e. getting to peach or dying?) (SORT OF DONE? but game just ends... should fix that probably maybe)[FRIDAY/WEEKEND]

## TODO BY MONDAY !!!!!!!!!!!!!!
- [x] make textfile graph
- [ ] fix maze/graph/screen and character sizes/peach
- [ ] generate graph with algorithm thing to check if valid edge and stuff to add to graph **ALGORITHM IMPLEMENTATION KIND OF SORT OF?**
- [x] ghost moving ~~thru BFS stuff~~
- [ ] endgame conditions

## WHAT WE ACTUALLY NEED TO BE DONE BY THURSDAY
- [x] textfile with walls/maze info
- [ ] new sprites for characters / import them correctly
- [ ] add edges to graph / make sure correct edges are being used
- [ ] move ghost with BFS and algorithm stuff
- [ ] calculate manhattan distance between ghost and player
- [ ] find nearest vertex and make ghost move to that vertex every k seconds
- [ ] endgame conditions

## TODO BY THURSDAY / BONUS???? IDEK
- [x] sprite importing and making sure they move properly
- [ ] multiple ghosts every x amount of seconds and have those 
- [ ] coins / points system
- [ ] readme? idk




REFERENCES:
- https://stackoverflow.com/questions/18826788/converting-an-image-to-a-rect
