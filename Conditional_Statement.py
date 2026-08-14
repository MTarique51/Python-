light = input("light:")

if(light=="red"):
    print("Stop")
elif(light == "yellow"):
    print("Look")
elif(light == "green"):
    print("Go")
else:
    print("Light is nor working")


# Conditional Statements(Single Line if / Ternary Operator)
# <var> = <val1> if <condition> else <val2>
food = input("food: ")
eat = "Yes" if food == "cake" else "no"
print("Able to eat ? ", eat)

            # OR #

# <stt1> if <condition> else <stt2>
food = input("food: ")
print("sweet") if food == "cake" or food =="Jalebi" else print("No sweet")
