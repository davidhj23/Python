'''
temperature = 31

if temperature > 30:
    print("It is a hot day")
else:
    print("It is not a hot day")
'''

name = input("Enter your name: ")
name_lenght = len(name)

if name_lenght < 3:
    print("name must be at least 3 characters")
elif name_lenght > 50:
    print("name must be maximun 50 characters")
else:
    print("name looks good")

