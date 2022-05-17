#WPP to compute the value of n+nn+nnn
a=int(input("Enter an integer : "))
num1=int("%s"% a)
num2=int("%s%s"%(a,a))
num3=int("%s%s%s"%(a,a,a))
print(num1+num2+num3)
