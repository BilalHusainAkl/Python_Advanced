#WPP to delete an element from tuple.
name=('','birth','innocence','death','salvation')
print((name))
name1=list(name)
#print(type(name1))
position = int(input('Enter your number'))

name1.pop(position)
#print(name1)

name = tuple(name1)
print(name)

