# Exercises

# 1 Print a string
print("This is my first program")

# 2 Declare, set a value and Print Variables
myInt = 200
print(myInt)

# 3 Perfome simple arithmetic operations
a = 20
c = a * 100
print(c)

# 4 Execute conditional statements
myVal = 800
if myVal > 0:
    print("It is a positive number")
elif myVal == 0:
    print("The value is 0")
else:
    print("It is a negative number")

# 5 Declare and print an array using a for-loop
myArray = [20, 43, 23, 50, 200]
for n in myArray:
    print(n)

# 6 Execute a break statement  using a for-loop
shoppingList = ["bread", "water", "butter", "chips", "soda"]
for item in shoppingList:
    print(item)
    if item == "butter":
        break

print("------")
# 7 Declare and print a variable using a while-loop
Score = 60
while Score < 90:
    print(Score)
    Score += 5

print("-------")
# 8 Execute a break statement  using a while-loop
myVal = 70
while myVal < 90:
    print(myVal)
    if myVal > 80:
        break
    myVal += 2