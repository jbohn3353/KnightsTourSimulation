# KnightsTourSimulation
A simulation of the classic computational problem of Knight's Tour seeking to find the total number of unique tours from each starting position.

The simulation works by generating a near 0% fail rate tour that is then compared to a list of unique tours for a given starting position. If the new tour generated is found in the list of prior unique tours, nothing happens. If the new tour generated is not found, it is then added to the list. 

However, this simulation currently has some limitations:
  * I am not currently tracking total number of tours generated for each position. This means that if a position has simply had more simulations run on it, it will likely have more unique tours.
  * The simulation will theoretically never be guarenteed to contain every possible solution, it will simply approach 0% new solutions on simulations
