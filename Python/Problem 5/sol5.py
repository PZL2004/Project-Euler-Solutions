"""
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time

start = time.time()

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def LCM(a, b):
    return (a*b)/ GCD(a, b)

def smallest_num(n):
    ans = 1
    for i in range(2, n+1):
        ans = LCM(ans, i)
    return ans

if __name__ == "__main__":
    print(int(smallest_num(20)))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")