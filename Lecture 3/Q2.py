# WAP to check palindrome

list1 =[1,2,1] 
list2 =[1,2,3] 

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("List1 : Palimdrome")
else:
    print("List1 : Not Palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("List2 : Palimdrome")
else:
    print("List2 : Not Palindrome")


