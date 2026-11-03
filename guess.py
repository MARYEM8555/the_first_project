import random
secret = random.randint(1, 100)
attempts = 0
print("Guess the number between 1 and 100!")
while True:
    guess = int(input("Your guess:"))
    attempts += 1
    if guess < secret:
        print("Too Low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You found it in {attempts} attempts.")
        break 