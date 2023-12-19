"""
Longest Collatz Sequence
Which starting number, under one million, produces the longest chain?
"""
import time

start = time.time()

def collatz_sequence(n):
    a = [n]
    while n != 1:
        if n % 2 == 0:
            n /= 2
            a.append(n)
        else:
            n = 3*n + 1
            a.append(n)
    return a

def longest_collatz_sequence(limit):
    lst_of_collatz_sequences = []
    for i in range(2,limit):
        lst_of_collatz_sequences.append(collatz_sequence(i))
    
    max_len_sequence = 0
    for i, seq in enumerate(lst_of_collatz_sequences):
        if len(seq) > max_len_sequence:
            max_len_sequence = len(seq)
            starting_num = seq[0]
    
    return starting_num

if __name__ == "__main__":
    print(longest_collatz_sequence(1_000_000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")