''' crear una tuple '''
# name = () #esto es una tupla vacia
# name =( 'item1', 'item2', 'item3', 'item4', ... ) # esto es una tupla con datos
# fruits = ('banana', 'orange', 'mango', 'lemon')

'''se puede usar el method de len() para saber el tamaño de una tupla'''
# tamaño_tuple = len(fruits)
# print(tamaño_tuple)

'''iterar sobre la tuple con numeros negativos'''
# print(fruits[::-1])

'''extraer en partes dandole el index de inicio y donde terminara'''
# print(fruits[0:])
# print(fruits[0:1])

'''extraer en partes dandole el index negativos de inicio y donde terminara'''
# print(fruits[-3:-1])
# print(fruits[-3:])


'''extraer los datos de una tuple a una list y  de list a tuple'''
# list_fruits = [*fruits] #primera forma de pasar de una tuple a list
# tuple_list = list(fruits) # segunda forma de pasar de una tuple a list
# print(list_fruits)

# list_fruits = tuple(list_fruits) # forma de pasar de una list a tuple es la unica forma de hacerlo
# print(list_fruits)

'''checar si existe un valor en una tuple con el metodo 'in' esto retornara un boolean'''
# print('banana' in fruits)
# print('melon' in fruits)

'''unir dos o mas tuplas con el operador '+' '''
# vegetables = ('onion', 'potato', 'carrot', 'garlic', 'cabbage')
# fruits_vegetables = (*fruits, *vegetables) # se puede unir dos o mas tuples con este metodo
# fruits_vegetables = fruits + vegetables # este es el metodo por defecto
# print(fruits_vegetables)

'''eliminar tuple usando 'del' y borrara la tuple'''
# del fruits
# print(fruits)

