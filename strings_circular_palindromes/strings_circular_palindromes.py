# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
https://www.hackerrank.com/challenges/circular-palindromes

steps:
1. get inputs
2. get k-rotations
3. find palidrome (need to handle odd and even length strings)

Walk each character
check for even length palidrome (>= 4 chars)
check for odd length palidrome (>= 3 chars)
print ONLY the max len palidrome for each rotation

even length palindrome
set start to current index
set end to index + 1
if start and end is within string length
test if start == end
continue if equal
decrement start, increment end


odd length palidrome
set start to index - 1
set end to index + 1
strore current index in buffer
if start and end is within string length
test if start == end
continue if equal
decrement start, increment end



'''

def rotate(s, rotations):
    ''' returns a k-length rotated string (shift 1st character to end of string)
    	s  string
    	rotations  number of rotations 
    '''
    rbuf = [x for x in s]
    for k in range(rotations):
    	temp = rbuf.pop(0)
    	rbuf.append(temp)
    
    rotated = ''.join(rbuf)
    return rotated

def test_pal(s, buf, start, end):
	''' generic routine to find palindrome
	
		s 		the string to search in
		buf 	a list containing current palindrome
		start 	index of start of substring
		end 	index of end of substring
		
		Note: buf is needed to distinguish between odd and even cases
	'''
	length = len(s)
	output = buf
	
	# keep searching as long as within length of s
	while start >= 0 and end <= length-1:
		
		if s[start] != s[end]:
			return output
		else:
			# got a match
			buf.insert(0, s[start])
			buf.append(s[end])

		# move to outer location			
		start = start - 1
		end = end + 1
	
	return output
	
def test_even_pal(s, idx):
	''' return list containing chars of even palindrome '''	
	start = idx
	end = idx + 1
	
	return test_pal(s, [], start, end)

def test_odd_pal(s, idx):
	''' return list containing chars of odd palindrome '''
	start = idx - 1
	end = idx + 1

	return test_pal(s, [s[idx]], start, end)

def find_palindrome(s):
	'''
		find both odd-length and even-length palidromes
		Assume minimum length of even palindrome is 4 and odd palindromes are min 3
		
		returns the largest of the palindromes
	'''
	
	max_len = 0
	
	length = len(s)
	for idx in range(length):
		buf = test_even_pal(s, idx)
		size = len(buf)
		if size > 3:
			# even palidromes must be at least 4 or more chars
			#print ''.join(buf)
			#print len(buf)
			if size > max_len:
				max_len = size

		buf = test_odd_pal(s, idx)
		size = len(buf)
		if size > 2:
			# odd palidromes must be at least 3 or more chars
			#print ''.join(buf)
			if size > max_len:
				max_len = size

	return max_len

if __name__ == '__main__':
	DEBUG = True

	if DEBUG:
		#num_chars = 7
		#s = 'cacbbba'
		num_chars = 13
		s = 'aaaaabbbbaaaa'

		print num_chars
		print s
		print '---------------'
	else:
		num_chars = input()
		s = raw_input()
	
	
	rotated = s
	for n in range(num_chars):

		max_len = find_palindrome(rotated)
		print max_len
		
		rotated = rotate(rotated, 1)
		print rotated
