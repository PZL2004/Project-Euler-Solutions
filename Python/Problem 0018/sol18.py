"""
Find the maximum total from top to bottom of the triangle below:
"""
import time

start = time.time()

def max_path_sum(tree):
    for i in range(len(tree)-2, -1, -1): # last -1 very important 
        for j in range(len(tree[i])):
            tree[i][j] += max(tree[i+1][j], tree[i+1][j+1])
    return tree[0][0]

# change path to whatever yours is
with open("Python/Problem 0018/tree.txt", "r") as f:
    tree = []
    for i in f:
        tree.append(list(map(int, i.split(" ")))) #very cool

if __name__ == "__main__":
    print(max_path_sum(tree))
    end = time.time()
    print(f"Computation time: {1000*(end-start)} ms")
