# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool together  dollars for ice cream. On any given day, the parlor offers a line of  flavors. Each flavor, , is numbered sequentially with a unique ID number from  to  and has a cost, , associated with it.

Given the value of  and the cost of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose two flavors such that they spend their entire pool of money () during each visit. For each trip to the parlor, print the ID numbers for the two types of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. You must print the smaller ID first and the larger ID second.


Takeaway
problem requires returning the IDs (index), not the cost of ice cream

sorted(list) returns a new sorted list. Must ensure list is integers, not string
' '.join(list) to concatenate a list of strings

'''

def get_sorted_list(nums):
    if len(nums) < 2:
        return ''
    sorted_list = sorted(nums)
    #print (sorted_list)
    return ' '.join([str(item) for item in sorted_list])

# match() - return True if sum 
def is_sum(total, v1, v2):
    if v1 + v2 == total:
        return True
    return False

# find_2_flavors() return space-separated integers of IDs
def find_2_flavors(pool, flavors, flavlist):

    for i in range(flavors):
        for j in range(flavors):
            # check match as long as not itself
            if j != i:
                if is_sum(pool, flavlist[i], flavlist[j]):
                    # sort IDs in increasing order. IDs are offset by 1
                    output = [i+1, j+1]
                    return get_sorted_list(output)
    return ''


# get_trip_details as tuple
def get_trip_details():
    # return pool as int, flavors as int, and flavlist as list of ints
    pool = input()
    flavors = input()
    flavlist_arg = raw_input().split(' ')
    flavlist = [int(f) for f in flavlist_arg]
    return (pool, flavors, flavlist)

def main():
    # iterate thru trips
    trips = input()
    for trip in range(trips):
        (pool, flavors, flavlist) = get_trip_details()
        #print pool, flavors, flavlist
        ids = find_2_flavors(pool, flavors, flavlist)
        print ids

if __name__ == '__main__':
    main()