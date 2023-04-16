'''
loop de while se crea:
    wuile condicion:
        print('la condicion se cumple') 
    else: 
        print('la condicion no se cumple')
    
el "else" es cuando la condicion ya no se cumpla ejecutara lo que este despues del 'else'
el "break" es para que deje de ejecutar el loop
el "continue" es cuando llege a eso ejecute algo y salte a la siguiente iteracion
        
'''

# count = 0
# while count < 5:
#     print('la condicion se cumple')
#     count += 1
# else:
#     print('la condicion ya no se cumple')

''' example con break'''
# count = 0
# while count < 5:
#     print('la condicion se cumple')
#     if (count == 3):
#         print('la condicion llego a 3')
#         break

#     count += 1
# else:
#     print('la condicion ya no se cumple')

'''example con continue'''
# count = 0
# while count < 10:
#     if count < 3:
#         # esto se ejecutara  hasta que el 'if'
#         # deje de cumplir y seguira con el while loop
#         print('olis')
#         count += 1
#         continue

#     print(count)
#     count += 1
# else:
#     print('termino la iteracion')


'''
loop de for se usa en a list, a tuple, a dictionary, a set, or a string se crea de la diferente forma:
    for 'iterador' in 'array, tuple, dictionary, set, string':
        print('ejecutara esto hasta que termine la iteracion del array, tuple, dictionary, set, string')
'''
# numbers = [0, 1, 2, 3, 4, 5]

# for number in numbers: # number es un nombre temporal que solo existira hasta que  terminne de iterar la list
#     print(number)

'''loop con string'''
lenguage = 'python'

# for letter in lenguage:
#     print(letter)

# for i in range(len(lenguage)):
#     print(lenguage[i])

'''loop con tuple'''
# numbers = (0, 1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)

''' loop con dictionary esto retornara las keys'''
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# for key in person:
#     print(key)

# for key, value in person.items():
#     print(f'{key}: {person[key]}')

'''loops en set esto retorna las companias en forma aleatoria ya que los sets son aleatorios'''
# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# for company in it_companies:
#     print(company)

'''recordatorio 'break' se usa para detener algo antes de tiempo dependiendo la condicion anidada'''
# numbers = (0, 1, 2, 3, 4, 5)

# for number in numbers:
#     if (number == 4):
#         print(f'se cumplio la condicion de {number}')
#         break
#     print(number)

'''recordatorio  continue se usa para brincar una iteracion del for '''
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if(number == 3):
#         continue
#     print(f'el numero podria ser: {number}') if number != 5 else print(f'este es el ultimo numero: {number}')
# print('termino el loop')
# valor = list(range(1,11))

'''range es para darle un rango de donde a donde tomara  valores range(start, end, step) -> range(0,11,1)'''
# for number in range(1, 11):
#     print(f'el numero es: {number}')

''' anidando loop dentro de otro loop '''
# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_marred': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# for key in person:
#     print(f'{key}: {person[key]}')

#     if (key == 'skills'):
#         for skill in person[key]:
#             print(f'    skiil: {skill}')
#         continue
#     if (key == 'address'):
#         for adress in person[key]:
#             print(f'    {adress}: {person[key][adress]}')

''' el pass '''
# for number in range(6):
#     pass
#     print(number)
