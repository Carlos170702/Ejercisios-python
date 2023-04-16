''' para concatenar variables con texto es haci'''
# print(f'{1} + {2} = {1+2}')

''' para concatenar variables con texto y que es valor es o quieres que sea double y que despues del punto tenga 2 o 3 etc caracteres es haci'''
# print(f'{1} + {2} = {1+ 2:.2f}')

''' 
para extraer valores de un strin o list o dictionarys etc...
pero en este caso en pyton si el array o la variable tiene 6 caracteres tienes que hacer 6 variables 
si no no se puede
    1. destructura un string
    2. destructura un list
'''
# name = 'carlos'
# a,b,c,d,e,f = name
# print(a)

# full_name = ['carlos', 'daniel', 'cruz', 'perez']
# first_name, second_name, firt_last_name, second_last_name = full_name
# print(f'{first_name}\n{second_name}\n{firt_last_name}\n{second_last_name}')

''' 
metodos de los strings
    1: capitalize 
    2: count() recibe como parametro lo que buscara en el string y podria o no recibir de donde a donde quiere empezar y terminar
    3: endswith() se usa para ver si un string termina en un una determinada palabra o letra y te devuelve un boolean
    4: expandtabs() se usa para dar spacing el cual recibe la cantidad de espacios que dara, pero el string debe de contener en vez de espacios > (\t) 
    5: find() se usa para encontrar una letra o palabra en un estring y te retorna el indice donde esta esa palabra o letra y si no lo encuentra te retorna -1
    6: replace() se usa para remplazar una palabra por otra como parametro recibe que palabra quiere cambiar y el segundo parametro es cual es la nueva palabra
'''

name = 'carlos'
# print(name.capitalize())
# print(name.count('l'))  # * todo el string
# print(name.count('l', 3, 5))  # * empieza de la pocicion 3 al 5
# print(name.endswith('s'))
# print('carlos\tdaniel'.expandtabs())
# print(name.find('a'))
# print('carlos daniel'.replace('daniel', 'cruz'))

''' Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'. '''
# firt_word = 'Thirty'
# second_word = 'Days'
# Thirty_word = 'of'
# fourty_word = 'Python'
# full_word = (f'{firt_word} {second_word} {Thirty_word} {fourty_word}')
# print(full_word)

''' Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'. '''
# firt_word = 'Coding'
# second_word = 'For'
# Thirty_word = 'All'
# full_word = ( f'{firt_word} {second_word} {Thirty_word}' )
# print(full_word)

''' Declare a variable named company and assign it to an initial value "Coding For All". '''
company = 'Coding for All'
''' Print the variable company using print(). '''
# print(company)
''' Print the length of the company string using len() method and print(). '''
# print(len(company))
''' Change all the characters to uppercase letters using upper() method '''
# print(company.upper())
''' Change all the characters to lowercase letters using lower() method. '''
# print(company.lower())
''' Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All. '''
# print(company.capitalize())
# print(company.title()) #* todas las primeras letras de la cadena de texto los vuelve mayuscula
# print(company.swapcase()) #* combierte todas las letras que andan en mayusculas a minusculas y viseversa
''' Cut(slice) out the first word of Coding For All string. '''
# print(company.split(" ")[0])
''' Check if Coding For All string contains a word Coding using the method index, find or other methods. '''
# print(company.index('Coding'))
''' Replace the word coding in the string 'Coding For All' to Python. '''
# print(company.replace('Coding', 'Csode'))
''' Change Python for Everyone to Python for All using the replace method or other methods. '''
# print('Python for Everyone'.replace('Python for Everyone',company))
''' Split the string 'Coding For All' using space as the separator (split()) . '''
# print(company.split())
''' "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma. '''
# print('Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'.split(","))
''' What is the character at index 0 in the string Coding For All. '''
# print(company[0])
''' What is the last index of the string Coding For All. '''
# print(len(company) - 1)
''' What character is at index 10 in "Coding For All" string. '''
# print(company[10])
''' Create an acronym or an abbreviation for the name 'Python For Everyone'. '''
# destructur_word = 'Python For Everyone'.split()
# print(f'{destructur_word[0][0]}{destructur_word[1][0]}{destructur_word[2][0]}'.upper())
''' Create an acronym or an abbreviation for the name 'Coding For All'. '''
# destructur_word = company.split()
# print(f'{destructur_word[0][0]}{destructur_word[1][0]}{destructur_word[2][0]}'.upper())
''' Use index to determine the position of the first occurrence of C in Coding For All. '''
# print(company.index('C'))
''' Use index to determine the position of the first occurrence of F in Coding For All. '''
# print(company.index('f'))
''' Use rfind to determine the position of the last occurrence of l in Coding For All People. '''
# print('Coding For All People'.rfind('l'))#* obtiene la posicion de la ultima l que existe en el string
''' Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
# print('You cannot end a sentence with because because because is a conjunction'.index('because'))
''' Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
# print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
''' Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
# print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
''' Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
# print('You cannot end a sentence with because because because is a conjunction'.find('because'))
''' Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction' '''
# print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
''' Does ''Coding For All' start with a substring Coding? '''
# print('Coding For All'.startswith('Coding'))
''' Does 'Coding For All' end with a substring coding? '''
# print('Coding For All'.endswith('Coding'))
''' '   Coding For All      '  , remove the left and right trailing spaces in the given string. '''
# print('   Coding For All      '.strip(' '))#*lo que hace es que elimina todos los espacion que existen
'''
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
'''
# print('30DaysOfPython'.isidentifier())
# print('thirty_days_of_python'.isidentifier())
''' he following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string. '''
# print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
''' 
Use the new line escape sequence to separate the following sentences. 
    I am enjoying this challenge.
    I just wonder what is next.
'''
# print('I\nam\nenjoying\nthis\nchallenge.')
# print('I\njust\nwonder\nwhat\nis\nnext.')
'''
Use a tab escape sequence to write the following lines.
    Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''
# print('Name\tAge\tCountry\tCity')
# print('Asabeneh\t250\tFinland\tHelsinki')
''' 
Use the string formatting method to display the following: 
    radius = 10
    area = 3.14 * radius ** 2
    The area of a circle with radius 10 is 314 meters square.
'''
# radius = 10
# area = 3.1416 * radius ** 2
# print(f'The area of a circle with radius {str(radius)} is {int(area)} meters square.')
'''  
Make the following using string formatting methods: 
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
'''
# print(f'8 + 6 = { 8+6 }')
# print(f'8 - 6 = { 8-6 }')
# print(f'8 * 6 = { 8*6 }')
# print(f'8 / 6 = { 8/6:.2f}')
# print(f'8 % 6 = { 8%6 }')
# print(f'8 // 6 = { 8//6 }')
# print(f'8 ** 6 = { 8**6 }')
