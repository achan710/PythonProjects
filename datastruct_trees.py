
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
	
	def display(self):
		print '---start---'
		print self.key
		print self.left
		print self.right
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
		self.__traverse(self.root)

	def __insert(self, node, key):
	
		print key
		#if node is not None:
			#node.display()
		
		if node == None:
			# found position to insert node
			node = Node(key)
			#print node.key
			
		else:
			# pitfall: originally was checking left.key. But left does not exist yet
			
			# search left if key is less than, or right if key is greater than
			if key < node.getkey():
				self.__insert(node.getleft(), key)
			else:
				self.__insert(node.getright(), key)
		
	def __traverse(self, node):
		if node == None:
			return
		
		self.__traverse(node.getleft())
		print node.key
		self.__traverse(node.getright())
	
	def debug(self):
		print '\n'
		print self.root.key
		print self.root.left
		print self.root.right

def test_node():

	a = Node(5)
	b = Node(6)
	c = Node(7)
	
	items = [a,b,c]
	output = ' '.join( [str(x.key) for x in items] )
	print output

def test_bst():
	T = BinarySearchTree()
	T.add(5)
	T.add(6)
	T.add(2)
	T.walktree()
	
	T.debug()


if __name__ == '__main__':

	#test_node()
		
	test_bst()


	
