# python3

import sys
import threading

class Node:
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


def inorder(root):

	if root is None:
		return

	inorder(root.left)
	print(root.data, end=' ')
	inorder(root.right)


def compute_height(n, parents):
    	# create an empty dictionary
	dict = {}

	# create `n` new tree nodes, each having a value from 0 to `n-1`,
	# and store them in a dictionary
	for i in range(n):
		dict[i] = Node(i)

	# represents the root node of a binary tree
	root = None

	# traverse the parent list and build the tree
	for i, e in enumerate(parents):

		# if the parent is -1, set the root to the current node having the
		# value `i` (stored in `dict[i]`)
		if e == -1:
			root = dict[i]
		else:
			# get the parent for the current node
			ptr = dict[e]

			# if the parent's left child is filled, map the node to its right child
			if ptr.left:
				ptr.right = dict[i]
			# if the parent's left child is empty, map the node to it
			else:
				ptr.left = dict[i]

	# return root of the constructed tree
	return root


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
