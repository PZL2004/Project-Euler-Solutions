"""
Longest Collatz Sequence
Which starting number, under one million, produces the longest chain?
"""
import time

start = time.time()

def collatz_sequence_count(n):
    # recursive collatz count. Used some pseudo code to wrap my head around it. Recursion weird but saves computation time
    while n > 1: # added while else as a base case so that a RecursionError does not occur
        if n in vals: # if n has already been calculated, why do it again?
            return vals[n]
        elif n % 2 == 0:
            vals[n] = 1 + collatz_sequence_count(n/2) # Collatz(n) = Collatz(n/2) + 1 if even n
        else:
            vals[n] = 2 + collatz_sequence_count((3*n + 1)/2) # Collatz(n) = Collatz((3n+1)/2) + 2 if odd n
        return vals[n]
    else:
        return -1

limit = 1_000_000
vals = dict()

max_count = 0
corresponding_n = 0
for n in range(limit//2 + 1, limit): # Collatz(2n) > Collatz(n) so no need to check n <= limit//2
    if collatz_sequence_count(n) > max_count:
        max_count = collatz_sequence_count(n)
        corresponding_n = n

if __name__ == "__main__":
    print(corresponding_n)
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")