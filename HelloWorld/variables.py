# How Python code gets executed
'''
print('David Henriquez')
print('o----')
print(' ||||')
print('*' * 10)
'''

# Variables
'''
price = 10              # integers
rating = 4.9            # floats
name = 'David'          # string
is_published = True     # boolean
print(is_published)
'''

'''
full_name = 'John Smith'
age = 20
is_new = True
'''

# Receiving inputs
'''
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name +  ' likes ' + favorite_color)
'''

# Type conversion
'''
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2024 - int(birth_year)
print(type(age))
print(age)
'''

'''
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
'''

# Strings
course = "Python's Course for beginners"
print(course)
course = 'Python for "beginners"'
print(course)
course = '''
Python 
for 
beginners
'''
print(course)
course = 'Python for beginners'
print(course[0])
print(course[-2])
print(course[0:5])
print(course[1:])
print(course[3:5])
another = course[:]
print(another)
name = 'Jennifer'
print(name[1:-1])

# Formatted Strings
first = 'John'
last = 'Smith'
message = first + ' [' + last + ']'
msg = f'{first} [{last}]'
print(message)
print(msg)

# String methods
course = 'Python for Beginners'
print(course.upper())
print(course.lower())
print(course)
print(course.find('o'))
print(course.find('O'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))
print('Python' in course)
print('python' in course)
print(course.title())

# Arithmetic operations
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
x = 10
x = x + 3
x += 3 # Augmented assign operator
x -= 3 # operator
print(x)

# Operator Precedence
x = 10 + 3 * 2
print(x)
x = 10 + 3 * 2 ** 2
print(x)
x = (10 + 3) * 2 ** 2
print(x)
x = (2 + 3) * 2 - 2
print(x)

# Math functions
x = 2.9
print(round(x))
x = 2.9
print(abs(-x))
x = 2.9
print(abs(-x))
