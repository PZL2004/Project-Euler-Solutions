"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time

start = time.time()

def sum_of_squares(n):
    return sum([i**2 for i in range(1, n+1)])

def square_of_sum(n):
    return sum(range(1, n+1))**2

if __name__ == "__main__":
    print(square_of_sum(100) - sum_of_squares(100))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")