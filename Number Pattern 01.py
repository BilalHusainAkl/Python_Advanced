#WPP to print pattern in Python #pattern01
n=int(input("Enter number of rows : "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    
