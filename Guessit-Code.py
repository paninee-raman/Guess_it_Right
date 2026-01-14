import random
number=random.randint(1,50)
max_num=5
print("Guess the number between 1 and 50")
print("You have 5 attempts")

for i in range(max_num):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("You won!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
else:
    print("Game over! The number was",number)
