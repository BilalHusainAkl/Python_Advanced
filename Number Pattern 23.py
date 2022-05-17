#WPP to print patter #pattern23
n=int(input("Enter number of rows: "))
for i in range(n-1,-1,-1):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(0,i+1,1):
        print(n-j,end=" ")
    print()
