"""
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? (British use of and)
"""
import time

start = time.time()

def letter_counter_1000(n):
    #ONLY WORKS FOR [1,1000]. Similar, but different, logic would be needed for n > 1000
    if n == 0:
        return 4
    elif n < 0 or n > 1001:
        return "Choose a number [1,1000]"
    
    n_to_str = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
                8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
                14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen",
                19:"nineteen", 20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty",
                70:"seventy", 80:"eighty", 90:"ninety"} # do you say ten zero? lol
    
    count = 0
    for i in range(1,n+1):
        a = i // 1000 % 10 #thousands digit
        b = i // 100 % 10 # hundreds digit
        c = i //10 % 10  # tens
        d = i % 10 # ones digit
        
        if a:
            count += (len(n_to_str[a]) + 8) # thousand
        if b:
            count += (len(n_to_str[b]) + 7) # hundred
            if c or d: # only an "and" if there is a b != 0, and c or d != 0 for numbers [1,1000]
                count += 3 # and
        if c == 1:
            count += len(n_to_str[10*c + d]) # tens and ones if one of the teens
        else:
            count += (len(n_to_str[10*c]) + len(n_to_str[d])) # tens and ones if not teens

    return count

if __name__ == "__main__":
    print(letter_counter_1000(1000))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")