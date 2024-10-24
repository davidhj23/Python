weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    print(f"You are {weight / 2} kilograms")
elif unit.upper() == 'K':
    print(f"You are {weight * 2} pound")
else:
    print("You did not entered a valid unit")


