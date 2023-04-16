'''create a new set el set ordena los valores asendentemente'''
# st = {}
# st= set()

fruit = {'banana', 'orange', 'melon', 'kiwi', 'pineapple'}
list_fruit = ['banana', 'orange', 'melon', 'kiwi', 'pineapple']

'''obtener el tamaño del 'set' '''
# lenght_fruits = len(fruit)
# print(lenght_fruits)

'''checar si existe un valor en un "set" el cual retorna un booleano'''
# value_fruit = 'pineapple' in fruit
# print(value_fruit)

'''agregar nuevo item pero lo que no deja es modificar los valores'''
# fruit = {*fruit, 'lime', 'apple'} # primera forma de agregar valore
# fruit.add('lime') # esta es la segunda forma la cual se usa el metodo add
# print(fruit)

''''añadir varios valores a un "set" es con el metodo update() el cual recibe como parametro la lista de los valores a agregar
esto se puede ahorrar con el metodo spread que se mostro anterior mente
'''
# fruit = {*fruit, 'lime', 'apple', 'blueberry', 'grape'} # primera forma de agregar valores
# fruit.update( ['lime', 'strawberry', 'blueberry', 'grape'] ) # esta es la segunda forma
# print(fruit)

'''
eliminar un valor de el "set" se hace con el metodo remove() el cual recibe como parametro el valor a eliminar
pero si no lo encuentra retornara un error, pero ahi otro metodo que es el discart() el cual no devuelve ningun valor
'''
# fruit.remove('blueberry') # esto dara un error
# fruit.discard('banana') # esto no dara ningun error pero tampoco eliminara nada
# print(fruit)

'''
para eliminar un valor aleatoriamente con el metodo pop() aleatoriamente algun valor de el "set" y el cual retornara que valor elimino
pero este no tiene la opcion de pasarle como parametro el valor que decea eliminar es solo aleatoriamente
'''
# print(fruit.pop())

'''para limpiar un "set" es con el metodo de clear() que deja limpio el set'''
# fruit.clear()
# print(fruit)

'''para eliminar un "set" es con el metodo de "del" seguido del set a eliminar '''
# del fruit
# print(fruit)

'''
para comvertir de set a list se hace con el metodo de list() y para comvertir una lista a un set es con el metodo de set() 
pero igual se puede hacer con el metodo spread 
'''
# metodo spread
# set_list_fruit = [*fruit] # esto es de un set a una lista
# list_set_fruit = { *list_fruit } # esto es de una lista a un set
# metodos de python
# set_list_fruit = list(fruit)
# list_set_fruit = set(list_fruit)
# print(list_set_fruit)


'''
unir dos set eto se hace con los metodos de: 
set.update(set_unir) el cual recibe como parametro el set que quiere unir y retorna un nuevo valor de set
set.union(set_unir) el cual recibe como parametro el set que quiere unir y retorna un nuevo valor de set
pero tambien se puede hacer con el metodo de spread 
'''
vegetables = {'carrot', 'onion', 'garlic', 'cucumber'}
# fruit_vegetables = fruit.union(vegetables)
# fruit_vegetables = fruit.update(vegetables)
# fruit_vegetables = { *fruit, *vegetables }
# print(fruit_vegetables)

''''
para encontrar lo valores que existen de un set a otro set es con el metodo de intersection() el cual devuelve un nuevo set con los valores encontrados
'''
# A = {1, 2, 3, 4}
# B = {9, 7, 5, 6}
# items_founds= A.intersection(B)
# print(items_founds)

'''
para checar si todos los datos que estan en el 'set_1' estan en el 'set_2' esto se hace con con metodos los cuales reciben como 
parametro el set que quieren verificar:
    issubset() el cual checa si todos los valores de el 'set_1' estan precentes en el 'set_2'
    issuperset() el cual checa si todos los valores del 'set_2' estan precentes en el 'set_1' y al menos tenga 1 valor de mas 
'''
# a = {1, 2, 3, 4}
# b = {1, 2, 3}
# value = a.issubset(b) #lo q hace es que checa si los valores que tiene el set de a existen en el set b si si retorna true
# lo q hace es que checa si los valores de el set a existen en el b y superan
# value = a.issuperset(b)
# print(value)


''''
para saber la diferiencia que existen entre dos 'sets' se hace con el metodo de set.difference(set2) el cual retorna la diferiencia en un nuevo set
que hay entre set a set2
valor_mayor.difference(valor_menor) return > difference
'''
# a = {1, 2, 3, 4, 5, 6}
# b = {1, 2, 3}

# difference = a.difference(b)
# print(difference)


'''
para obtener los valores que en los dos sets tienen de diferiencia uno del otro es con el metodo de symmetric_difference() retorna un nuevo set
set.symmetric_difference(set2)
'''
# a = {1, 2, 3, 4, 5, 6}
# b = {1, 2, 3, 10}

# differences = a.symmetric_difference(b)
# print(differences)

'''
saber si dos sets tienen algo en comun con el metodo isdisjoint() esto retorna booleano dependiendo si del set tiene alguna variable en comun con el set2
false dara cuando si tenga valores en comun pero dara true cuando tenga valores diferentes
'''
# a = {1, 2, 3, 4, 5, 6}
# a = {0,0,0,0,0}
# b = {1, 2, 3, 10}
# print(a.isdisjoint(b) )
