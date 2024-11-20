"""
What is the total of all the name scores in the file?
"""
import time

start = time.time()

with open("Python/Problem 0022/names.txt", "r") as f:
    for i in f:
        names = sorted(i.replace("\"", "").split(","))

def sum_name_scores(names):
    total = 0
    for name in names:
        alphabetical_score = 0
        for j in name:
            alphabetical_score += (ord(j) - 64) # ord(A) = 65, ord(B) = 66, etc.
        index_score = names.index(name) + 1
        name_score = alphabetical_score * index_score
        total += name_score
    return total

if __name__ == "__main__":
    print(sum_name_scores(names))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")