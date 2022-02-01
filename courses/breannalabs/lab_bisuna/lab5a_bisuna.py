""" lab5a """
num = int(input("Enter a positive integer: "))

sum1 = 0
for i in range(1,num+1):
    print(i,end=' ')
    sum1 += i

print("\nThe sum is ", sum1, ".",sep="")