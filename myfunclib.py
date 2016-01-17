"""
functions working with lists

"""
def double_list(x):
    # takes  a list and doubles each value
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

def total(numbers):
    #function returns the sum of a list of numbers
    result = 0
    
    for i in range(0, len(numbers)):
        result += numbers[i]
    return result

"""
functions working with strings

"""
def join_strings(words):
    # Takes a list of words and joins them
    result = ""
    for i in range(len(words)):
        result += words[i]
    return result


n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
     # Takes a single list and concatenates all the sublists that are part of it into a single list.
     results = []
     for numbers in lists:
         for i in numbers:
             print i
             results.append(i)
     return results

flatten(n)
