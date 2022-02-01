"""
Lab 6a - Function that returns the factorial
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def factorial(num):
    """
    Function to compute and return factorial
    paramemter: num - compute the factorial of positive integer
    return: factorial of num, 0 if negative parameter
    """
    if num < 0: # only positive integers
        return 0
    if num == 0: # for factorial of 0 or negative number
        return 1
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact


def main():
    print("Factorial of 10:", factorial(10))
    print("Factorial of 15:", factorial(15))


if __name__ == "__main__":
    main()
