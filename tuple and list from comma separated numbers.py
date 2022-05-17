#WPP to generate list and a tuple with comma separated numbers.
values = input("Enter comma separated numbers : ")
list=values.split(",")
print("List : ",list)
tuple=tuple(list)
print("Tuple : ",tuple)
