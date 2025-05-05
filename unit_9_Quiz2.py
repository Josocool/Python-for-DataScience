import random

# random answer
answer = random.randint(1, 100)
tries = 0

print("Guess a number between 1 to 100")

while True:
    try:
        guess = int(input("Enter a number: "))
        tries += 1

        if guess > answer:
            print("Lower!")
        elif guess < answer:
            print("Higher!")
        else:
            print(f"Congratulations. Total try = {tries}")
            break
    except ValueError:
        print("Please enter a valid integer.")
