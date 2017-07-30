
import itertools

def swap(s, i, j):
	arr = [x for x in s]
	temp = s[i]
	arr[i] = s[j]
	arr[j] = temp
	swapped = ''.join(arr)
	return swapped

def find_perms(s):
	perms = []
	for idx in range(len(s)):
		for  jdx in range(len(s)):
			#print idx, jdx
			perms.append(swap(s, idx, jdx))
			#print idx, jdx

	return perms

class Container():
	''' Keep track of unique items and count '''
	
	def __init__(self):
		self.struct = {}
		
	def add(self, item):
		''' only add if unique, otherwise increment counter '''
		if item not in self.struct:
			self.struct[item] = 1
			print item
		else:
			self.struct[item] = self.struct[item] + 1
			print item, 'dup'

	def total(self):
		return len(self.struct)
		
	def display(self):
		print 'total = {}'.format(self.total())
		for (k, v) in self.struct.items():
			print (k, v)
		print('\n')
	
	def sum(self):
		sum = 0
		for (k, v) in self.struct.items():
			sum = sum + v
		return sum
		
	def get_list(self):
		return self.struct.keys()

def search(s, b):
	''' Return true if sub string is found in string b
		s the sub string
		b the string
	'''
	if s in b:
		return True
	return False

def main_2():
	''' use our own swap method to find permutations of inputs in b '''
	
	b = 'babcabbacaabcbabcacbb'
	con = Container()
	
	inputs = ['abbc', 'bbca', 'bcab', 'cabb']
	
	# loop all possible inputs, add to list in Container
	for s in inputs:
		perms = find_perms(s)
		for p in perms:
			con.add(p)
		con.display()
	
	print con.sum()

	# find permutations
	print 'find permutations'
	perms = con.get_list()
	for p in perms:
		if search(p, b):
			print p

def main_1():
	''' use built-in permutation '''
	
	struct = {}
	inputs = ['abcd', 'bcda', 'cdab', 'dabc']
	total = 0
	for s in inputs:
		perms = itertools.permutations(s, 4)
		for p in perms:
			if p not in struct:
				struct[p] = 0
			else:
				struct[p] = struct[p] + 1
				print 'dup'
			total = total + 1
			print p, total
		print '\n'

	for (k, v) in struct.items():
		print k, v
	
	print 'total = {}'.format(len(struct))

#main_1()
main_2()
