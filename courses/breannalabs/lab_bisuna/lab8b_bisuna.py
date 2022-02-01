"""
Lab 8b - Recursive function that returns the summation of the given parameter
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""
import sys

def my_sum(val):
    """
    Function returns summation of val1 recursively
    paramemter: val number to get summation
    return: summation
    """
    if val > 0:
        return val + my_sum(val-1)
    return 0


def main():
    """ driver """
    # increase recursion depth
    # even at 6000 recursion limit, my computer can only handle 3922
    sys.setrecursionlimit(6000) 
    num = 3922
    # after 3922 the results become unstable, works sometimes
    print("The sum from 1 to",num,"is", my_sum(num))


if __name__ == "__main__":
    main()
