#  L I S T     M E T H O D S


# list = ["pple" , "banana" , "mango"]          # all methods will be apply on this also 
list = [2 , 1 , 3 ]
print("ORIGINAL LIST : ",list)

list.append(4)         # add one element at the end
print("add one element at the end: ",list)

list.sort()            # sort in ascending order 
print("sort in ascending order: ",list)

list.sort(reverse=True)       # sort in descending order
print("sort in descending order: ",list)

list.reverse()         # reverse list
print("reverse list: ",list)

list.insert(1, 1111)   # insert element at index
print("insert element at index: ",list)

list.pop(1)            # removes element at index
print("removes element at index: "list)