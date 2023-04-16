# age = [22, 19, 24, 25, 26, 24, 25, 24]
'''Convert the ages to a set and compare the length of the list and the set, which one is bigger?'''
# age_set = {*age}
# lenght_age = len(age)
# lenght_age_set = len(age_set)

# if( lenght_age > lenght_age_set ):
#     print(f'the length of the age list: {lenght_age} is greater than the length of the age set:{lenght_age_set}')
# else:
#     print(f'the length of the age set: {lenght_age_set} is greater than the length of the age set:{lenght_age}')
    
'''
Explain the difference between the following data types: string, list, tuple and set
el string es el que solo son letras rodeadas por parentesis
list es aquella que tiene diferentes datos ya sea string, int, double, hasta bibliotecas
tuples es como las listas pero las tuples no se pueden modificar sus valores mas agregar nuevos datos si y sis metodos son menos a comparado de las listas 
set son aquellas que se  crea con parentesis o con llaves y no se puede modificar sus valores mas bien si añadir y eliminar valores
'''

'''
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split 
methods and set to get the unique words.
'''
word = 'I am a teacher and I love to inspire and teach people'
words = word.split(" ")
word_set = set(words)
print(word_set)


