#WPP to print patter #pattern06
n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i,-1,-1):
        print(n-j,end=" ")
    print()
