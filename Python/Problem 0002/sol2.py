"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import time

start = time.time()

def fibonacci_numbers(limit):
    #initializing list and index
    a = [1, 2]
    i = 0
    while True:
        #finds the next term
        n= a[i]+a[i+1]
        # appends next fibonacci number and increases index only if the fibonacci number is less than the limit
        if n < limit:
            a.append(n)
            i += 1
        # breaks the loop if not
        else:
            break
    return a


f = fibonacci_numbers(4_000_000)

# initializes the sum
total = 0
for val in f:
    # only adds to the sum of the fibonacci number if even
    if val % 2 == 0:
        total += val

if __name__ == "__main__":
    print(total)
    end = time.time()
    print(f"Compute time {1000*(end-start)} ms")