"""
What is the 10,001st prime number?
"""
import time

start = time.time()

def sieve(n):
    a = [True for i in range(n+1)]
    p = 2
    while p**2 <= n:
        if a[p]:
            for i in range(p**2, n+1, p):
                a[i] = False
        p += 1
    
    primes = []
    for p in range(2, n+1):
        if a[p]:
            primes.append(p)
    return primes
            

if __name__ == "__main__":
    print(sieve(105000)[10000]) #index starts at 0
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")