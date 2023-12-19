"""
What is the sum of the digits of the number 2^1000?
"""
import time

start = time.time()

def sum_of_digits_power(b, ex):
    return sum(int(i) for i in str(b**ex))

if __name__ == "__main__":
    print(sum_of_digits_power(2,1000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")

