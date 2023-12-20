"""
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import time

start = time.time()

def sum_proper_divisors(n):
    total = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            total += i
    return total

def abundant_nums():
    MAX = 28123
    abundant_ns = []
    for i in range(12,MAX):
        a = sum_proper_divisors(i)
        if a > i:
            abundant_ns.append(i)
    return abundant_ns

def sum_of_nums_that_not_sum_of_abundant_nums():
    abundant_ns = abundant_nums()
    abundant_sums = set()
    
    for i in range(len(abundant_ns)):
        for j in range(i, len(abundant_ns)):
            sum_ = abundant_ns[i] + abundant_ns[j]
            if sum_ <= 28123:
                abundant_sums.add(sum_)
    
    return 395465626 - sum(abundant_sums) # 395465626 is from sum of consecutive numbers formula: n(n+1)/2 for n = 28123
                

if __name__ == "__main__":
    print(sum_of_nums_that_not_sum_of_abundant_nums())
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")