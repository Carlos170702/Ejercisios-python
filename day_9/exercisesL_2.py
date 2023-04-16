'''Write a code which gives grade to students according to theirs scores:'''
# students = input('Enter the number of students: ')

# score_students = []
# final_score = []
# abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
#               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# for i in range(int(students)):
#     firt_score = int(
#         input(f'Enter the firt score del estudiante -> {i + 1}: '))
#     second_secore = int(
#         input(f'Enter the second score del estudiante -> {i + 1}: '))
#     score_students.append(
#         {'firt_score': firt_score, 'second_score': second_secore})

# for score in score_students:
#     final_score.append(score['firt_score'] + score['second_score'])

# scores_ordened = sorted(final_score, reverse=True)

# for i, cali in enumerate(scores_ordened):
#     score_one = score_students[i]['firt_score']
#     scores_second = score_students[i]['second_score']
#     print(f'the score of student {i + 1} = {score_one} - {scores_second} -> {abecedario[i]}')

'''
Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, 
the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, 
July or August, the season is Summer
'''
# month = input('Enter the month: ').capitalize()

# if (month == 'September' or month == 'October' or month == 'November'):
#     print('The season is Autumn')
# elif (month == 'December' or month == 'January' or month == 'February'):
#     print('The season is Winter')
# elif (month == 'March' or month == 'April' or month == 'May'):
#     print('The season is Spring')
# elif (month == 'June' or month == 'July' or month == 'August'):
#     print('The season is Summer')
# else:
#     print('the month is invalid')

'''
The following list contains some fruits:
    fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
'''
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input('Enter your fruit: ')
# print('That fruit already exists in the list') if ( fruit in fruits ) else fruits.append(fruit)
# print(fruits)
