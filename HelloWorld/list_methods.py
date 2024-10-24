numbers = [5, 2, 1, 5, 7, 4, 7]
numbers.append(20)

print(numbers)

print()
numbers.insert(1, 21)
print(numbers)

print()
numbers.remove(5)
print(numbers)

print()
numbers.pop()
print(numbers)

print()
print(numbers.index(4))

print()
print(50 in numbers)

print()
print(numbers.count(5))

print()
numbers.sort()
print(numbers)

print()
numbers.reverse()
print(numbers)

print()
numbers_copy = numbers.copy()
print(numbers_copy)

# Remove duplicates in a list
print()
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

print()
numbers.clear()
print(numbers)