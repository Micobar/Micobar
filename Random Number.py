import random

x = random.randrange(1,10)
i = 0
while i <= 5:
    y = int(input("Guess the number: "))
    if x == y:
        print("You guessed it!")
        break
    else:
        print("Nah, this is not the one")
        i += 1

if x != y:
    print(f"Game Over, You Loose! The number was {x}")
else:
    print("Nice One! Game Over!")