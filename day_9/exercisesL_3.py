'''
Here we have a person dictionary. Feel free to modify it!
    person={
        'first_name': 'carlos daniel',
        'last_name': 'cruz perez',
        'age': 20,
        'country': 'mexico',
        'is_marred': false,
        'skills': ['HTML','CSS','JavaScript', 'ReactJs','NextJs', 'PHP', 'MYSQL', 'Typescript','java'],
        'address': {
            'street': 'Calle "X" de mayo',
            'zipcode': '30000'
        }
    }
'''
person = {
    'first_name': 'carlos daniel',
    'last_name': 'cruz perez',
    'age': 20,
    'country': 'mexico',
    'is_marred': False,
    'skills': ['HTML', 'CSS', 'JavaScript', 'ReactJs', 'NextJs', 'PHP', 'MYSQL', 'Typescript', 'Java', 'React Native'],
    'address': {
        'street': 'Calle "X" de mayo',
        'zipcode': '30000'
    }
}

''''* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.'''
# if ('skills' in person):
#     all_skills = len(person['skills'])
#     if (all_skills % 2 == 0):
#         print(person['skills'][all_skills // 2 - 1] + ',' + person['skills'][all_skills // 2 ])
#     else:
#         print(person['skills'][all_skills // 2])
# else:
#     print('the key does not exist')

'''* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.'''
# skill_find = 'python'
# if ('skills' in person):
#     found_skill = skill_find in person['skills']
#     print(f'{skill_find} is found in the person dictionary') if( found_skill ) else print(f'{skill_find} is not found in the person dictionary')
# else:
#     print('the key does not exist')

'''
* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
    Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
    else print('unknown title') - for more accurate results more conditions can be nested!
'''
# skills = person['skills']
# if ('ReactJs' in skills and 'Node' in skills and 'MongoDB' in skills):
#     print('he is a fullstack developer')
# elif ('JavaScript' in skills and 'ReactJs' in skills):
#     print('he is a front-end developer')
# elif ('Node' in skills and 'MongoDB' in skills and 'Python' in skills):
#     print('he is a back-end developer')
# else:
#     print('he is a normal person XD')

'''
* If the person is married and if he lives in Finland, print the information in the following format:
    "Asabeneh Yetayeh lives in Finland. He is married."
'''
# def Verify_is_marred(is_marreed):
#     return 'married' if is_marreed else 'not married'

# if (person['is_marred'] != True and person['country'] == 'mexico'):
#     full_name = person['first_name'] + ' ' + person['last_name']
#     country = person['country']
#     is_marred = person['is_marred']
#     print(f'{full_name} lives in {country}. He is { Verify_is_marred(is_marreed=is_marred) }')
