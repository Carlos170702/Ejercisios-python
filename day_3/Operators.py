age = 20
height = 1.50
complex_number = 1 + 1j

# # calcule the area of the triangle
# base_triangle = input('please write the base of triangle')
# height_triangle = input('please write the height of triangle')
# area_of_triangle = (int(base_triangle) * int(height_triangle)) / 2
# print('the area of the triangle is :', area_of_triangle)

# # calcule the perimeter of the triangle
# a = input('please write the value of side a')
# b = input('please write the value of side b')
# c = input('please write the value of side c')
# perimeter_of_triangle = int(a) + int(b) + int(c)
# print('the perimeter of the triangle is: ', perimeter_of_triangle)

# # area and perimeter of the rectangle
# length_of_rectangle = int(input('please write the length of the rectangle'))
# width_of_rectangle = int(input('please write the width od the rectangle'))
# area_of_rectangle = length_of_rectangle * width_of_rectangle
# perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)
# print('the area of the rectangle is : ', area_of_rectangle)
# print('the perimeter of the rectangle is : ', perimeter_of_rectangle)


# area and circunference of the circle
# radius_circle = int(input('please write the radius of the circle'))
# PI = 3.1416
# area_of_circle = PI * radius_circle**2
# circunference_of_circle = 2 * PI * radius_circle
# print('the area of the circle is :', area_of_circle)
# print('the circunference of the circle is :', circunference_of_circle)

# slope of the y = 2x -2
# def calcule_of_intersection(ecuacion):
#     parts = ecuacion.split(" ")
#     a = float(parts[2][:-1])
#     b = float(parts[4])
#     intersection_in_x = -b / a
#     print('intersection in x is : ', intersection_in_x)
#     print('intersection in y is : ', b)
# calcule_of_intersection("y = 2x - 2")

# # falsy comparation
# length_python = len('python')
# length_dragon = len('dragon')

# if not (length_python > 0):
#     print('the lenght of the "python" is 0  ')
# else:
#     print('the lenght of the "python" is not 0  ')

# if not (length_dragon > 0):
#     print('the lenght of the "dragon" is 0  ')
# else:
#     print('the lenght of the "dragon" is not 0  ')


# # found the "on" in the other words
# python = 'python'
# dragon = 'gragon'

# if ('on' in python and 'on' in dragon):
#     print('"on" is found in the "python" and "dragon"')
# else:
#     print('"on" is not found in the "python" or "dragon"')

# found the "jargon" in the phrafe "I hope this course is not full of jargon"
phrase = 'I hope this course is not full of jargon'
word = 'jargon'

if (word in phrase):
    print('"jargon" is found in the phrase')
else:
    print('"jargon" is not found in the phrase')


# convert words int to float and float to string
lenght_python = len('python')
convert_float = float(lenght_python)
convert_string = str(lenght_python)
print(convert_string)


# check if the number is even or not
number = input('write the number')
remainder = int(number) % 2
if ( remainder == 0 ):
    print('the number is divisible')
else:
    print('the number is not divisible')

# check the floor division of 7 // 3  is equal to the number int(2.7)
floor_division = 7//3
number_converted = int(2.7)
if( floor_division == number_converted ):
    print('the numbers are equals')
else:
    print('the numbers are not equals')


# check type of "10" is equal to type 10
if ( type('10') == type(10) ):
    print('type of "10" is equal to type 10')
else:
    print('type of "10" is not equal to typr 10')

# check if converting "9.8" to int is equal to 10
if (int(float('9.8')) == 10):
    print('is equal')
else:
    print('is not equal')


# calculate pay of person
hours = int( input('write the hours') )
rate = int( input('write the rate') )
pay = hours * rate
print(pay)


# calculate the number of seconds a person can live
years = int(input('write the years'))
seconds_live = (((int(years) * 365) * 24)* 60) * 60
print(seconds_live, 's')

numbers = [
    '1 1 1 1 1',
    '2 1 2 4 8',
    '3 1 3 9 27',
    '4 1 4 16 64',
    '5 1 5 25 125'
]

for item in numbers:
    print(item)
