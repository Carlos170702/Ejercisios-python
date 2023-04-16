# names_brother = ('jose', 'gustavo', 'pedro', 'jaimito')
# names_sister = ('maria', 'rosa', 'jane')
# siblings = (*names_brother, *names_sister)
# family_members = [*siblings, 'reynaldo', 'manuela']

'''Unpack siblings and parents from family_members'''
# print(family_members)
# parents_members = family_members[-2:]
# sibling_members = family_members[0:int(len(family_members) - 2)]
# print(parents_members)
# print(sibling_members)

'''Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.'''
# fruits = ('apple', 'melon', 'kiwi', 'pear')
# vegetables = ('garlic', 'onion', 'brawberry')
# animals = ('leon', 'bird', 'monkey', 'cat', 'dog')
# food_stuff_tp = (*fruits, *vegetables, *animals)
# print(food_stuff_tp)

'''Change the about food_stuff_tp tuple to a food_stuff_lt list'''
# food_stuff_lt = [*food_stuff_tp]
# print(food_stuff_lt)

'''Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.'''
# all_food_stuff = len(food_stuff_lt)
# if (all_food_stuff % 2 == 0):
#     del food_stuff_lt[all_food_stuff // 2]
#     del food_stuff_lt[all_food_stuff // 2 - 1]
# else:
#     del food_stuff_lt[all_food_stuff // 2]
# print(food_stuff_lt)

'''Slice out the first three items and the last three items from food_staff_lt list'''
# last_food_staff_lt = len(food_stuff_lt) -1 
# del food_stuff_lt[0:2]
# del food_stuff_lt[-3:]
# print(food_stuff_lt)

'''Delete the food_staff_tp tuple completely'''
# del food_stuff_tp
# print(food_stuff_tp)

'''
Check if an item exists in tuple:
    Check if 'Estonia' is a nordic country
    Check if 'Iceland' is a nordic country

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''
# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# print('Estonia' in nordic_countries)
# print('Iceland' in nordic_countries)