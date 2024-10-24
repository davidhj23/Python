secret_number = 5
i = 0

while i <= 2:
    guess = int(input('Guess: '))
    if guess == secret_number:
        print("You won!")
        break
    i += 1
else:
    print("You loose!")