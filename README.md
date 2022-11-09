# 2048solver
This application solves a modified version of the classic 2048 game.

Differences:
  1. 2048s are wall tiles
  2. Win condition is when only one non-wall tile remains
  3. Wall tiles cannot be be moved
  4. No new tiles are generated during play (unless you choose to set them yourself)

To run:
>python app.py

To play:
>Set size of the board and toggle through cells to set their starting states

>Click "solve" to generate the most optimal moveset to win the game

>Use arrow keys and follow along to verify yourself.


If state can't be won within 15 moves, the 'solve' button will tell you so. 

This is due to:
  1. Total sum of starting tiles is not equivalent to a normal 2048 tile piece (2, 4, 8, 16, 32, ..etc)
      -> I.E., tiles cannot be combined into one
  2. A wall is blocking movement of tiles
  
