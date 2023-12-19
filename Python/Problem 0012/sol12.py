"""
What is the value of the first triangle number to have over five hundred divisors?
"""
import time
from math import sqrt

start = time.time()

def highly_div_triangle_num(limit, number_of_divisors):
    triangle_nums = [sum(range(1, i+1)) for i in range(1,limit+1)]
    for i in range(len(triangle_nums)):
        divisor_count = 0
        for j in range(2, int(sqrt(triangle_nums[i]))+1):
            if triangle_nums[i] % j == 0:
                divisor_count += 2
        if divisor_count >= number_of_divisors:
            return triangle_nums[i]
    

if __name__ == "__main__":
    print(highly_div_triangle_num(12375, 500)) # some arbitrarily large number to catch the case, the solution is the 12375th triangle number
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")