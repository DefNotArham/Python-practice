import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))

    if guess == num:
        print("You guessed it!")
        break
    elif guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        print("Wrong!")
