#function in python
#wpp to create a function for addition

def addition(a,b):
    print('addition=',a+b)


def substraction(a,b):
    if a>b:
        print(a-b)
    else:
        print(b-a)

def multiplication(a,b):
    print('multiplication=',a*b)

def division(a,b):
    if (a,b==0):
        print('plz check your input value')
    else:
        print('division=',a/b)


print('1-Addition','\n2-Substraction','\n3-Multiplication','\n4-Division','\n5-quit')

choice = 0
num1= float(input('Enter first number'))
num2 = float(input('Enter second number'))
choice = int(input('Enter your choice'))

#calculator logic
if choice ==1:
    addition(num1,num2)
if choice ==2:
    substraction(num1,num2)
if choice ==3:
    multiplication(num1,num2)
if choice ==4:
    division(num1,num2)


        
