'''se crea entre llaves como el de los set'''
person = {
    'first_name': 'carlos daniel',
    'last_name': 'cruz perez',
    'age': 20,
    'country': 'comitan',
    'is_married': False,
    'slkills': ['HTML', 'CSS', 'Javascript', 'reactJS', 'nextJS', 'react native'],
    'address': {
        'street': 'calle 5 de mayo',
        'zipcode': '30040'
    }
}

'''saber cuantos valores ahi "key"="value" en el dictionary '''
# print(len(person))

'''hacer referencia de un valor en el dictionary se hace con dictionary['key del dictionary'] si se le da un valor que no existe dara un error como
de no existe ya que no existe en el dictionary existe un metodo llamado get() que lo que hace es que si no existe el valor debuelve un none mas no error'''
# print(f'mi nombre es: {person["first_name"]} {person["city"]}') #este ejemplo retorna error si no existe
# print(f'mi nombre es: {person.get("city")}') # este retorna none si no existe

'''añadir un nuevo valor a el dictionary es con ( dictionary['nombre'] = 'valor' ) '''
# person['city'] = 'mexico'
# person['slkills'].append('MYSQL')
# print(person)

'''para modificar un dictionary es igual al de agregar ( dictionary['variable_update'] = 'new_value' ) '''
# person['address']= 'calle av.libertad'
# print(person)

'''checar si existe algun valor en el dictionary con la key y te retorna un boolean'''
# print('city' in person)

'''
para eliminar un valor en el dictionary ahi tres opciones:
dictionary.pop(key_eliminar) se le da como parametro el valor para eliminar y retornara el valor eliminado
dictionary.popitem() elimina el ultimo valor te retornara el valor eliminado
del dictionary[key_eliminar] este se le pone el item a eliminar 
'''
# person.pop('address') #esto retornara el valor eliminado sin su key solo su valor
# person.popitem() #esto retorna el valor eliminado con su key 
# del person['address'] #esto nada mas elimina el valor no retorna nada
# print(person)

'''para cambiar de dictionary a list esto es con el metodo de items() el cual hace una lista de tuplas'''
# dictionary_list = person.items()
# print(dictionary_list)

'''para limiar un dictionary es con el metodo de clear()'''
# person.clear()
# print(person)

'''para eliminar un dictionary es con el "del" '''
# del person
# print(person)

'''copar un dictionary en otro dictionary es con el metodo copy'''
# new_dict = person.copy()
# print(new_dict)

'''para obtener todos los valores en una lista pero separa los valores y las keys cada uno ocupa un valor en la lista'''
# values = person.values()
# print(values)

