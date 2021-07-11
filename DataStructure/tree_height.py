# python3

import sys
import threading

class Node:
        def __init__(self, data):
            self.left = None
            self.right = None
            self.data = data

def compute_height(n, parents):
    # Replace this code with a faster implementation 
    nodes= [n]
    for i in range(n):
        nodes[i] = Node()
    for child_index in range(n):
        if parents[child_index] == -1:
            root = child_index
        else:
            nodes[parents[child_index]].append(nodes[child_index])
        # height = 0
        # current = vertex
        # while current != -1:
        #     height += 1
        #     current = parents[current]
        # max_height = max(max_height, height)
    return nodes


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
