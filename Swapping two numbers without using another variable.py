# Python code to swap two numbers without using another variable
x = int(input('Enter first number : '))
y = int(input('Enter second number : '))
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
