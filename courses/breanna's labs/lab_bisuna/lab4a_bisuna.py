import random

magic = random.randint(1,10)

user1 = int(input("User 1, enter a number between 1 and 10: "))
user2 = int(input("User 2, enter a number between 1 and 10: "))

userd1 = abs(magic - user1)
userd2 = abs(magic - user2)

print("Magic Number:",magic)
if userd1 > userd2:
    print("User 2 guessed",user2,"which is closer to",magic,"than",user1)
else:
    print("User 1 guessed",user1,"which is closer to",magic,"than",user2)
