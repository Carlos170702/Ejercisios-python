'''Declare an empty list'''
vegetables = []

'''Declare a list with more than 5 items'''
fruits = ['banana', 'apple', 'pear', 'kiwi', 'melon']

'''Find the length of your list'''
# print(len(vegetables))
# print(len(fruits))

'''Get the first item, the middle item and the last item of the list'''
# print(fruits[0])
# print(fruits[2])
# print(fruits[len(fruits)-1])

'''Declare a list called mixed_data_types, put your(name, age, height, marital status, address)'''
mixed_data_types = ['carlos', 20, 55, 'soltero', 'calle 5 de mayo']

'''Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.'''
it_companies = ['facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon' ]


'''Print the list using print()'''
# print(mixed_data_types)
# print(it_companies)

'''Print the number of companies in the list'''
# print(len(it_companies))

'''Print the first, middle and last company'''
# print(it_companies[0])
# print(it_companies[int((len(it_companies)-1) / 2)])
# print(it_companies[len(it_companies)-1])

'''Print the list after modifying one of the companies'''
# it_companies[len(it_companies)-1] = 'instagram'
# print(it_companies)

'''Add an IT company to it_companies'''
# it_companies = [*it_companies, 'instagram']
# print(it_companies)

'''Insert an IT company in the middle of the companies list'''
# middle_index = int((len(it_companies)-1) / 2)
# it_companies.insert(middle_index, 'instagram')
# print(it_companies)

'''Change one of the it_companies names to uppercase (IBM excluded!)'''
# company_upper = it_companies[2].upper()
# print(company_upper)

'''Join the it_companies with a string '#' '''
# join_companies = '#'.join(it_companies)
# print(join_companies)

'''Check if a certain company exists in the it_companies list.'''
# company_exist = 'Microsoft' in it_companies
# print(company_exist)

'''Sort the list using sort() method'''
# it_companies.sort()
# print(it_companies)

'''Reverse the list in descending order using reverse() method'''
# it_companies.reverse() # forma con reverse
# reversed_companies = it_companies[::-1] # segunda forma de poner al reves
# print(reversed_companies)
# print(it_companies)

'''Slice out the first 3 companies from the list'''
# slice_companies = it_companies[0:3]
# print(slice_companies)

'''Slice out the last 3 companies from the list'''
# slice_last_companies = it_companies[-3:]
# print(slice_last_companies)

'''Slice out the middle IT company or companies from the list'''
# slice_middle_companies = it_companies[2:5]
# print(slice_middle_companies)

'''Remove the first IT company from the list'''
# company_removed = it_companies.pop(0)
# del it_companies[0]
# print(it_companies)

'''Remove the middle IT company or companies from the list'''
# last_company = len(it_companies) - 1
# middle_company = it_companies[( int(last_company / 2) )]
# middle_index_company = it_companies.index(middle_company)
# del it_companies[middle_index_company]
# print(it_companies)

'''Remove the last IT company from the list'''
# last_company = int(len(it_companies) - 1)
# del it_companies[last_company]
# print(it_companies)

'''Remove all IT companies from the list'''
# it_companies.clear()
# print( it_companies )

'''Destroy the IT companies list'''
# del it_companies
# print(it_companies)

'''
Join the following lists:
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
'''
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end_back_end = [*front_end, *back_end]
print(front_end_back_end)

''''After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.'''
full_stack =  [*front_end, *back_end]
index_Redux = full_stack.index('Redux') + 1
full_stack.insert(index_Redux, 'python')
full_stack.insert(index_Redux + 1, 'SQL')
print(full_stack)
