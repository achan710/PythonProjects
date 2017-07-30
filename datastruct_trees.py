
'''
pitfalls:
1. forgot to include self argument to all class methods
2. forgot to convert integer keys to string during printing



'''
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
	

class BinarySearchTree():
	
	def __init__(self):
		self.root = None


	def add(self, key):
		self.__insert(self.root, key)

	def walktree(self):
		self.__traverse(self.root)

	def __insert(self, node, key):
		if node == None:
			# found position to insert node
			node = Node(key)
			print node.key
			return

		# search left if key is less than, or right if key is greater than
		left = node.left
		if key < left.key:
			self.__insert(left, key)
		else:
			self.__insert(node.right, key)
		
	def __traverse(self, node):
		if node == None:
			return
		
		self.__traverse(node.left)
		print node.key
		self.__traverse(node.right)
	
	def debug(self):
		print self.root
		
if __name__ == '__main__':

	a = Node(5)
	b = Node(6)
	c = Node(7)
	
	items = [a,b,c]
	output = ' '.join( [str(x.key) for x in items] )
	print output
	
	T = BinarySearchTree()
	T.add(5)
	T.add(6)
	T.add(2)
	#T.debug()
	T.walktree()



	
