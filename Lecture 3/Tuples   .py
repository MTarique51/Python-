# TUPLE IS IMMUTABLE

tup = (2 , 1 , 5 , 9 , 4)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# tup[0] = 5       this is not allowed in tuple


# M E T H O D S     O F    T U P L E S


print("Value at index: ", tup.index(1))

print("No of 1: ",tup.count(1))