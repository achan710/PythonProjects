
def get_product_3(numlist):

	'''
	returns the largest product of 3 numbers from numlist

	This algorithm sorts numlist from smallest to largest
	then calculates the product for 2 conditions:
	1. the 3 most largest values
	2. 2 (potentially) negative values and the largest positive value
	'''

	# take the product of the 3 most largest values
	sorted_list = sorted(numlist)
	pos_product = sorted_list.pop() * sorted_list.pop() * sorted_list.pop()

	# take the product of 2 (potentially) negative values and largest postiive value
	sorted_list = sorted(numlist)
	neg_product = sorted_list[0] * sorted_list[1] * sorted_list.pop()

	# return the larger of the 2 calculations
	if pos_product > neg_product:
		return pos_product
	else:
		return neg_product

a=[4,2,5,60,234,4,52,23,2] #730080
b=[-203,0,12,4] #0  203,12,4
c=[-321,0,99,1,-2] # 99 1 0
d=[-3,7,234,-23,90] #234 90 7
e=[12,12,12,13,-14,-13] # 12 12 13


# put into testcases list
testlist = [a,b,c,d,e]

# loop test cases
for test in testlist:
	if len(test) < 3:
		# handle not enough operands case
		print 'Error: need at least 3 numbers'
	else:
		product = get_product_3(test)
		print 'largest product for list {0} = {1}'.format(test, product)
