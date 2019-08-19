import time
import random

MIN = 1
MAX = 100001

class Node():
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
		self.leftHeight = 0
		self.rightHeight = 0

class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self,data):
		self.root = self.insert_helper(self.root,data)

	def insert_helper(self,current,data):
		if current is None:
			return Node(data)
		elif current.data < data:
			current.right = self.insert_helper(current.right,data)
			current.rightHeight = current.right.rightHeight + 1

		elif current.data > data:
			current.left = self.insert_helper(current.left,data)
			current.leftHeight = current.left.leftHeight + 1

		difference = current.leftHeight - current.rightHeight
		if difference == 2:
			differenceLeft = current.left.leftHeight - current.left.rightHeight
			if differenceLeft == -1:
				current.left = self.left_rotate(current.left)
			current = self.right_rotate(current)
		elif difference == -2:
			differenceRight = current.right.leftHeight - current.right.rightHeight
			if differenceRight == 1:
				current.right = self.right_rotate(current.right)
			current = self.left_rotate(current)
		return current

	def left_rotate(self,unbalanced):
		pivot = unbalanced.right
		temp = pivot.left
		unbalanced.right = temp
		pivot.left = unbalanced
		self.adjust_height(unbalanced,pivot)
		return pivot

	def right_rotate(self,unbalanced):
		pivot = unbalanced.left
		temp = pivot.right
		unbalanced.left = temp
		pivot.right = unbalanced
		self.adjust_height(unbalanced,pivot)
		return pivot

	def adjust_height(self,unbalanced,pivot):
		if unbalanced.left is None:
			unbalanced.leftHeight = 0
		else:
			unbalanced.leftHeight = max(unbalanced.left.leftHeight,unbalanced.left.rightHeight) + 1

		if unbalanced.right is None:
			unbalanced.rightHeight = 0
		else:
			unbalanced.rightHeight = max(unbalanced.right.leftHeight,unbalanced.right.rightHeight) + 1

		if pivot.left is None:
			pivot.leftHeight = 0
		else:
			pivot.leftHeight = max(pivot.left.leftHeight,pivot.left.rightHeight) + 1

		if pivot.right is None:
			pivot.rightHeight = 0
		else:
			pivot.rightHeight = max(pivot.right.leftHeight,pivot.right.rightHeight) + 1



	def delete(self,data):

		pass

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
			return [node.data] + self.pre_order_traverse(node.left) + self.pre_order_traverse(node.right)
		return []

	def in_order(self):
		return self.in_order_traverse(self.root)
		
	def in_order_traverse(self,node):
		if node:
			return self.in_order_traverse(node.left) + [node.data] + self.in_order_traverse(node.right)
		return []

	def post_order(self):
		return self.post_order_traverse(self.root)

	def post_order_traverse(self,node):
		if node is None:
			return self.post_order_traverse(node.left) + self.post_order_traverse(node.right) + [node.data]
		return []

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

	def successor(self):

		pass

	def predecessor(self):

		pass

def main():
#	data = [13,10,15,5,11,16,4,6,3]
	data = [i for i in range(MIN,MAX)]
	binary_search_tree = BinarySearchTree()
	#random.shuffle(data)

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