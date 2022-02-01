sum1 = 0
num = 0

while num != -999:
    num = int(input("Enter a positive integer: "))
    if num == -999:
        break
    else:
        if num % 2 == 0:
            sum1 += num

print("The sum of the positive even integers entered is",sum1)
