import time
import random

MIN = 1
MAX = 100001

class Node():
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self,data):
		node = Node(data=data)

		current = self.root

		if current is None:
			self.root = node
			return node

		while(True):
			if current.data < node.data:
				if current.right is None:
					current.right = node
					return node
				else:
					current = current.right
			else:
				if current.left is None:
					current.left = node
					return node
				else:
					current = current.left

	# def delete(self,data):
	# 	pass

	def search(self,data):
		count = 0
		current = self.root
		while True:
			if current.data == data or (current.left is None and current.right is None):
				break
			elif current.data < data:
				current = current.right
			elif current.data > data:
				current = current.left
			count+=1

		return count

	def pre_order(self):
		return self.pre_order_traverse(self.root)

	def pre_order_traverse(self,node):
		if node is None:
			return []
		return [node.data] + self.pre_order_traverse(node.left) + self.pre_order_traverse(node.right)

	def in_order(self):
		return self.in_order_traverse(self.root)
		
	def in_order_traverse(self,node):
		if node is None:
			return []
		return self.in_order_traverse(node.left) + [node.data] + self.in_order_traverse(node.right)

	def post_order(self):
		return self.post_order_traverse(self.root)

	def post_order_traverse(self,node):
		if node is None:
			return []
		return self.post_order_traverse(node.left) + self.post_order_traverse(node.right) + [node.data]

	def minimum(self):
		current = self.root
		while current.left != None:
			current = current.left
		if current is None:
			return -9999999999999999
		return current.data

	def maximum(self):
		current = self.root
		while current.right != None:
			current = current.right
		if current is None:
			return 9999999999999999
		return current.data

	# def successor(self):
	# 	pass

	# def predecessor(self):
	# 	pass

def main():
#	data = [10,7,12,14,11,17,13,20,4,2,3,1]
	data = [i for i in range(MIN,MAX)]
	binary_search_tree = BinarySearchTree()
	random.shuffle(data)

	start = time.time()
	for i in data:
		binary_search_tree.insert(i)
	end = time.time()
	print("Total insert time :",end-start)
	comparisons = 0
	start = time.time()
	for i in range(MIN,MAX):
		comparisons+=binary_search_tree.search(i)
	end = time.time()
	print("Average search comparisons : ",comparisons/(MAX-1))
	print("Average search time: ",end-start)


if __name__ == '__main__':
	main()