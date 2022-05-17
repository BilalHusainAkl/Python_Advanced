#WPP to print patter #pattern07
n=int(input("Enter number of rows: "))
for i in range(n):
    for j in range(0,i+1,1):
        print(n-j,end=" ")
    print()
