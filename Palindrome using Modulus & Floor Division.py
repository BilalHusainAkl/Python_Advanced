#WPP to determine whether a number is palindrome or not.
n=int(input("Enter any number"))
temp=n
rev=0
while(n>0):
    abc=n%10
    rev=rev*10+abc
    n=n//10
    if(temp==rev):
        print("The number is Palindrome")
    else:
        print("The number isn't Palindrome")
