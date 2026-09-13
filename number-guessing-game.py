import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess == num:
        print("You guessed it!")
        break
    else:
        print("Wrong!")
