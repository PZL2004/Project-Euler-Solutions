"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time

start = time.time()

def sum_of_mult_of_3_or_5(limit):
    # initializing an empty list
    a = []
    # looping through all the numbers not including the limit
    for i in range(1, limit):
        # checking remainders
        if i % 3 == 0 or i % 5 == 0:
            # appending if remainder is 0
            a.append(i)
    
    #finding the sum of all the integers in the list and returning it
    return sum(a)

if __name__ == "__main__":
    print(sum_of_mult_of_3_or_5(1000))
    end = time.time()
    print(f"Compute time: {1000*(end-start)} ms")
