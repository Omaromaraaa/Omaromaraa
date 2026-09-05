import random 
print("🎲 Welcome to the Number guessing Game ")

secret_number = random.randint(1,10)
attempt = 0

while True:
    guess = int(input("Enter a number between 1 and 10 : "))
    attempt+=1

    if guess==secret_number:
        print(f"🎉 Correct You guessed the number in {attempt} tries.")
        break

    elif guess>secret_number:
        print("🔼 Too high ! Try again")

    else:
        print("🔽 Too low ! Try again")    