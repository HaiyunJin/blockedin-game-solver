# blockedin-game-solver
Solution to the Window Blocked-in game

Game link:
https://www.microsoft.com/en-us/store/apps/blocked-in/9wzdncrfjb0v

To solve the puzzle, the red block is labled as 1, empty space as 0, 
and horizontal block are labeled by odd number and the vertical block
are labeled by even number.

The scrpit works with python2.

There is an example of level 94:

initial94=[  
 2, 4, 7, 7,10,12,  
 2, 4, 0, 8,10,12,  
 2, 1, 1, 8, 0,12,  
 0, 3, 3, 0, 9, 9,  
 0, 0, 6, 0,11,11,  
 5, 5, 6,13,13, 0]

Change the permuation in the file download.

ChangeLog:  
2.3: Use dictionary for search and match  
2.2: Breath-first search  
2.1: Depth-first search  
2.0: Some junk  
