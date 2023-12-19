"""
Lattice Paths
How many such routes are there through a 20 x 20 grid?

This has to do with combinatorics since the order that we choose when to go 
right and down to get from the top left to the bottom right does not matter, and
the total Right's and Down's we need never changes.

Given a grid of l x w: we get (l+w) choose l. Since l = w in our case, we can simplify to
2n choose n. Using the commonly known formula, we get that 2n choose n equals (2n)!/(n!*(2n-n)!)
= (2n)!/(n!*n!) = (2n)!/(n!)^2
"""
import time
from math import factorial, gamma, pi, sqrt

start = time.time()

def paths_in_square_grid_factorial(n):
    return int(factorial(2*n)/(factorial(n))**2) # made int to remove #.0

def paths_in_square_grid_gamma(n):
    # wolfram alpha gives the following equality
    return round((((2**(2*n))*gamma(n+0.5))/(sqrt(pi)*gamma(n+1)))) # rounded bc of rounding error

if __name__ == "__main__":
    print(paths_in_square_grid_factorial(20)) # both are around same compute time for me
    #print(paths_in_square_grid_gamma(20))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")

