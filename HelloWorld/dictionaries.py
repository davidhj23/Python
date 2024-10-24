customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer)

print()
print(customer["name"])

print()
print(customer.get("birthdate"))

print()
customer["name"] = "Jack"
print(customer)

print()
print(customer.get("birthdate", "Jan 1 1980"))

'''
print()
print(customer["birthdate"])
'''

# program
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

phone = input("Phone: ")
for number in phone:
    print(numbers.get(str(number)))