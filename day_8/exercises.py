'''Create an empty dictionary called dog'''
dog = {}

'''Add name, color, breed, legs, age to the dog dictionary'''
dog['name'] = 'boby'
dog['color'] = 'white'
dog['breed'] = 'canina'
dog['legs'] = 4
dog['age'] = 10

'''Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary'''
student = {
    'first_name': 'carlos daniel',
    'last_name': 'cruz perez',
    'gender': 'hombre',
    'age': 20,
    'marital_status': 'soltero',
    'skills': ['javascript', 'html', 'css', 'reactjs', 'nextjs', 'react native'],
    'country': 'comitan chiapas',
    'city': 'mexico',
    'address': 'calle 5 de mayo',
}

'''Get the length of the student dictionary'''
# lenght_student = len(student)
# print(lenght_student)

'''Get the value of skills and check the data type, it should be a list'''
# lenght_skills = len(student['skills'])
# print(lenght_skills)

'''Modify the skills values by adding one or two skills'''
# student['skills'] = [*student['skills'], 'redux', 'typescript']
# print(student)

'''Get the dictionary keys as a list'''
# keys_student = student.keys()
# print(keys_student)

'''Get the dictionary values as a list'''
# values_student = student.values()
# print(values_student)

'''Change the dictionary to a list of tuples using items() method'''
# dic_list = student.items()
# print(dic_list)

'''Delete one of the items in the dictionary'''
# del student['skills']
# student.pop('age')
# student.popitem()
# print(student)

'''Delete one of the dictionaries'''
# del student
# print(student)
