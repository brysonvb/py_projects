import random

choice1 = input("Enter choice 1: ")
choice2 = input("Enter choice 2: ")

pick = random.randint(0,1)

if pick == 0:
    choice = choice1
else:
    choice = choice2

print("Random Selection Engine chooses:", choice)
