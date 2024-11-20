"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import time

start = time.time()

def fibonacci_digits(n):
    a, b = 1, 1
    index = 2
    while len(str(b)) < n:
        a, b = b, a + b
        index += 1
    return index


if __name__ == "__main__":
    print(fibonacci_digits(1000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")