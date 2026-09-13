import random

num = random.randint(1, 100)

while True:
    guess = int(input("Guess the number: "))
    guessCounter = 0

    if guess == num:
        print(f"You guessed it! It took you {guessCounter} guesses")
        break
    elif guess > num:
        print("Lower")
        guessCounter = guessCounter + 1
    elif guess < num:
        print("Higher")
        guessCounter = guessCounter + 1
