# type conversion (automatic conversion in python)
a = 2
b = 4.25
c = "3"

sum = a + b  # 2.0 + 4.25 => 6.25
print("Sum of int and float :",sum)


# Type Casting 
a , b = 1 , "2"
c = int(b)
sum = a + c
print("Sum after type casting:",sum)

d = 3.14
d = str(d)
print(type(d))