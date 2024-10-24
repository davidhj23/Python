names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[0])

print()
print(names[2])

print()
print(names[-1])

print()
print(names[-2])

print()
print(names[2:])

print()
print(names[2:4])

print()
print(names[:])

print()
names[0] = 'Jon'
print(names)

# Largest number in a list
print()
numbers = [3, 6, 2, 8, 4, 10]
largest = 0

for number in numbers:
    if number > largest:
        largest = number

print(largest)