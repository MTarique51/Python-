# WAP to askk the user to enter names of their 3 favorite movies and store them in a list

# Movies = []

# m1 = input("enter 1st movie: ")
# Movies.append(m1)
# m2 = input("enter 2nd movie: ")
# Movies.append(m2)
# m3 = input("enter 3rd movie: ")
# Movies.append(m3)
 
# print(Movies)


#  P A L I N D R O M E

list1 = [1,0,0,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("This is a Palindrome")
else:
    print(" This is Not a Palindrome")