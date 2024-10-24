for x in range(4):
    for y in range(4):
        print(f"({x},{y})")

print('')

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    print('x' * x)

print('')

numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)

print('')

numbers = [1, 1, 1, 1, 5]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)