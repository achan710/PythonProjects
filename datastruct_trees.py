
'''
pitfalls:
1. forgot to include self argument to all class methods
2. forgot to convert integer keys to string during printing



'''
import pdb


class Node():
	def __init__(self, key):
		self.left = None
		self.right = None
		self.key = key
		
	def setkey(self, key):
		self.key = key

	def getkey(self):
		return self.key
		
	def getright(self):
		return self.right
	
	def getleft(self):
		return self.left
	
	def isleaf(self):
		if self.left is None and self.right is None:
			return True
		return False
	
	def display(self):
		print '---start---'
		
		if self.left is not None:
			left = self.left.getkey()
		else:
			left = None
		if self.right is not None:
			right = self.right.getkey()
		else:
			right = None

		print "key={}, left={}, right={}".format(self.key, left, right)
		print '---end---'
	

class BinarySearchTree():
	
	def __init__(self):
		self.root = None

	def add(self, key):
		# pitfall: had to add a case to handle when root is None

		if self.root == None:
			self.root = Node(key)
		else:
			self.__insert(self.root, key)

	def walktree(self):
		print '\nWalking Tree'
		self.__traverse(self.root)
		
	def delete(self, key):
		self.__remove(self.root, key)

	def search(self, key):
		print 'Search for {}'.format(key)
		node = self.__find(self.root, key)
		if node is not None:
			print 'Found'
		else:
			print 'Not Found'

	def __remove(self, node, key):
		# return if node is None
		if node is None:
			return None

		# check for match
		if node.key == key:
			# update the node and return it

			# need to handle 3 cases			
			# 1. handle case where node has 0 children - set to None
			# 2. handle case where node has 1 child - just replace node with child
			# 3. handle case where node has 2 child - 
			# replace node with (smallest) right child and connect left children to new node

			node.display()
			if node.isleaf():
				# 1. handle case where node has 0 children - set to None
				node = None
			elif node.getleft() is None and node.getright() is not None:
				# 2. handle case where node has 1 child - just replace node with child				
				node = node.right
			elif node.getleft() is not None and node.getright() is None:
				# 2. handle case where node has 1 child - just replace node with child
				node = node.left
			else:
				# node must have 2 nodes
				temp = node.getleft()
				node = self.transplant(node.getright())
				node.left = temp

			return node

		else:
			# continue search
			if key < node.key:
				node.left = self.__remove(node.getleft(), key)
			else:
				node.right = self.__remove(node.getright(), key)

		return node

	def __find(self, node, key):

		# return if node is None
		if node is None:
			return None

		# check for match
		if node.key == key:
			return node
		else:
			# continue search
			if key < node.key:
				next = self.__find(node.getleft(), key)
			else:
				next = self.__find(node.getright(), key)

		return next

	def __insert(self, node, key):
		self.__insert2(node, key)

	def __insert1(self, node, key):

		print 'insert {}'.format(str(key))
		#print key
		#print node.getkey()

		# pitfall: originally was checking left.key. But left does not exist yet

		# search left if key is less than, or right if key is greater than		
		if key < node.getkey():
			if node.getleft() == None:
				node.left = Node(key)
			else:
				self.__insert1(node.getleft(), key)
			
			print 'left'
		else:
			if node.getright() == None:
				node.right = Node(key)
			else:
				self.__insert1(node.getright(), key)
			print 'right'


	def __insert2(self, node, key):
		''' insert method version 2 using recursion
			pitfall: had to return node at the end
		'''

		print 'insert {}'.format(str(key))
		
		if node is not None:
			node.display()
		else:
			print 'NULL'
		
		if node == None:
			node = Node(key)
			print 'create new {}'.format(str(key))
			return node
		else:
			if key < node.getkey():
				print 'left'
				node.left = self.__insert2(node.getleft(), key)

			else:
				print 'right'
				node.right = self.__insert2(node.getright(), key)
				node.display()

		# needed this return to update the tree
		return node

# 		this routine fails. adding 3 value is fine. the 4th value gets lost from tree
# 		print 'insert {}'.format(str(key))
# 		
# 		if node is not None:
# 			node.display()
# 		else:
# 			print 'NULL'
# 		
# 		if node == None:
# 			node = Node(key)
# 			print 'create new {}'.format(str(key))
# 			return node
# 		else:
# 			if key < node.getkey():
# 				print 'left'
# 				node.left = self.__insert2(node.getleft(), key)
# 
# 			else:
# 				print 'right'
# 				node.right = self.__insert2(node.getright(), key)
# 				node.display()

	def __traverse(self, node):
		if node == None:
			return
		
		self.__traverse(node.getleft())
		print node.key
		self.__traverse(node.getright())
	
	def debug(self):
		print self.root.key
		print self.root.left.key
		print self.root.right.key

def test_node():

	a = Node(5)
	b = Node(6)
	c = Node(7)
	
	items = [a,b,c]
	output = ' '.join( [str(x.key) for x in items] )
	print output

def test_bst():
	items = [5, 4, 7, 7, 8]
	T = BinarySearchTree()
	
	for i in items:	
		print '\nadding {}'.format(i)
		T.add(i)
		#T.walktree()

	#pdb.set_trace()
	T.walktree()
	
	T.search(8)
	
	T.delete(7)
	T.walktree()
	#T.debug()

def modify(node):
	node.key = 4
	return node

if __name__ == '__main__':

	#test_node()
		
	test_bst()
	
	#a = Node(5)
	#modify(a)
	#print a.key
# 	a = Node(5)
# 	
# 	insert(a, 7)
# 	insert(a, 4)
# 	insert(a, 5)
# 	print a.display()
	