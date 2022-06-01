#WPP to add an element in tuple.
name=('birth','innocence','death','salvation')
#print(type(name))
name1=list(name)
#print(type(name1))

element = input('Enter your element')
position = int(input('Enter your number'))

name1.insert(position,element)
#print(name1)

name = tuple(name1)
print(name)

