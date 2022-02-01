""" lab5a """
num = int(input("Enter a positive integer: "))

SUM1 = 0
for i in range(1,num+1):
    print(i,end=' ')
    SUM1 += i

print("\nThe sum is ", SUM1, ".",sep="")
