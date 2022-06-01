#WPP to solve the Tower of Hanoi problem.
def TOH(numbers,x,y,z):
    if numbers==1:
        print("Move disk 1 from rod {} to rod {}".format(x,z))
        return
    TOH(numbers-1,x,z,y)
    print("Move disk {} from rod {} to rod {}".format(numbers,x,z))
    TOH(numbers-1,y,x,z)
disc=3
TOH(disc,x='A',y='B',z='C')
