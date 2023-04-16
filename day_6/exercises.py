'''Create an empty tuple'''
empty_tuple = ()

'''Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)'''
names_brother = ('jose', 'gustavo', 'pedro', 'jaimito')
names_sister = ('maria', 'rosa', 'jane')
    
'''Join brothers and sisters tuples and assign it to siblings'''
siblings = (*names_brother, *names_sister)
# print(siblings)

'''How many siblings do you have?'''
number_siblings = len(siblings)
# print(number_siblings)

'''Modify the siblings tuple and add the name of your father and mother and assign it to family_members'''
family_members = [*siblings, 'reynaldo', 'manuela']
# print(family_members)