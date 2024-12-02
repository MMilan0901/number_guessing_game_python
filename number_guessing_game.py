import random

num = random.randint(0,10)
points = 3
print("Guess the number!")

while True:
    n = int(input())
    if n != num:
        print("Wrong guess!")
        
        points -= 1
        print("You have " + str(points) + " point(s) left.")
        
        if points == 0:
            print("Game over!")
            break
    else:
        print("Good guess!")
        print("Exiting the game...")
        break
