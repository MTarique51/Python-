age = int(input("enter age: "))
if(age >= 18):
    print("Can Vote")
elif(age < 18 and age > 5):
    print("Can't Drive")       #_ _ _ _  indentation
else:
    print("This is not Define")


                                        # HERE ARE SOME PRACTICE QUESTION 

# Grade based on marks
marks =int(input("enter marks: "))

if(marks >= 90):
    print("Grade: A")
elif(marks >= 80):
    print("Grade: B")
elif(marks >= 70):
    print("Grade: C")
else:
    print("Grade: D")


# Check the niumber is even or odd
num = 14

if(num%2 == 0):
    print("THE NUMBER ISEVEN")
else:
    print("THE NUMBER IS ODD")


# Find greatest number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a >= b and a >= c):
    print("largest number: ",a)
elif(b >= c):
    print("Largest number: ",b)
else:
    print("Largest number: ",c)



# Check the number is multiple of n
x = int(input("Enter the number: "))
if(x%2 == 0):
    print(x , " is multiple of 7")
else:
    print(x , " is not multiple of 7")
    