"""
Lab 8b - Recursive function that returns the summation of the given parameter
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""
import sys

def mySum(val):
    """
    Function returns summation of val1 recursively
    paramemter: val number to get summation
    return: summation
    """
    if val <= 0:
        return 0
    else:
        return val + mySum(val-1)


def main():
    # increase recursion depth
    sys.setrecursionlimit(6000) # even at 6000 recursion limit, my computer can only handle 3922
    num = 3922
    print("The sum from 1 to",num,"is", mySum(num)) # after 3922 the results become unstable, works sometimes


if __name__ == "__main__":
    main()
