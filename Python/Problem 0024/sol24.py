"""
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import time

start = time.time()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_permutation(digits, position):
    permutation = []
    k = position - 1
    available_digits = list(digits)
    
    for i in range(len(digits), 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        permutation.append(available_digits.pop(index))
        k %= fact
    
    return ''.join(permutation)


if __name__ == "__main__":
    print(get_permutation('0123456789', 1000000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")