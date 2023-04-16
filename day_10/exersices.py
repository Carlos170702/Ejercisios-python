'''Iterate 0 to 10 using for loop, do the same using while loop.'''
# for number in range(0, 11):
#     print(number)

# i = 0
# while i < 11:
#     print(i)
#     i += 1

'''Iterate 10 to 0 using for loop, do the same using while loop.'''
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1

# for i in range(10, -1, -1):
#     print(i)


'''
Write a loop that makes seven calls to print(), so we get on the output the following triangle:
    #
    ##
    ###
    ####
    #####
    ######
    #######
'''
# i = 0
# while i < 7:
#     print('#' * (i + 1))
#     i += 1

# for i in range(7):
#     print('#' * (i + 1))

'''
Use nested loops to create the following:
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
'''
# i = 0
# while i < 8:
#     f = 0
#     print()
#     i += 1
#     while f < 7:
#         print('#', end=' ')
#         f += 1

# for i in range(8):
#     print()
#     for f in range(8):
#         print('#', end=' ')


'''
Print the following pattern:
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
'''
# for i in range(11):
#     print(f'{i} * {i} = {i*i}')

# i = 0
# while i < 11:
#     print(f'{i} * {i} = {i*i}')
#     i += 1

'''Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.'''
# skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

# for skill in skills:
#     print(skill)


'''Use for loop to iterate from 0 to 100 and print only even numbers'''
# for i in range(0, 101, 2):
#     print(f'This is the index {i}')

'''Use for loop to iterate from 0 to 100 and print only odd numbers'''
# for i in range(101):
#     if (i % 2 == 1):
#         print(f'This is the index {i}')