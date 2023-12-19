"""
Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

start = time.time()

def largest_palindromic_num_prod_3_digits():
    max_palindrome = 0
    for i in range(100,1000):
        for j in range(i, 1000):
            n = i * j
            if n > max_palindrome and str(n) == str(n)[::-1]:
                max_palindrome = n
    
    return max_palindrome

if __name__ == "__main__":
    print(largest_palindromic_num_prod_3_digits())
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")