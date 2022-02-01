""" lab5b """
SUM1 = 0
NUM = 0

while NUM != -999:
    NUM = int(input("Enter a positive integer: "))
    if NUM != -999:
        if NUM % 2 == 0:
            SUM1 += NUM
    else:
        break

print("The sum of the positive even integers entered is",SUM1)
