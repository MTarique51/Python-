str1 = "This is a string.\nwe are creating it  in python"
str2 = 'This is a string. \twe are creating it in python'
str3 = """This is a string"""
str4 = "Apna"
print(str1)
print(str2)

# concatination
print(str3+str4)

# length of string
print("Length:",len(str1))
final_str = str3 + " " + str4
print("length of final str:",len(final_str))

# Indexing
print("Value at this index:",str3[5])

#Slicing(with +ve indexing)
print("part of the string:",str3[0:4])
print("part of the string:",str3[:12])
print("part of the string:",str3[5: ])

#Slicing(with -ve indexing)
print("part of the string:",str4[-3:-1])
print("part of the string:",str4[-2:])
print("part of the string:",str4[:-3])