"""
Lab 7 - Function to return the minimum of 2 parameters
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def min2(val1, val2=0):
    """
    Function returns minimum of the 2 parameters
    paramemter: val1 - value 1, val2 - value 2 default 0
    return: minimum value
    """
    if val1 > val2:
        return val2
    elif val2 > val1:
        return val1
    else: # numbers are equal, return either
        return val1


def main():
    """ driver """
    in1 = int(input("Enter an int: "))
    in2 = int(input("Enter an int: "))
    print("The minimum of", in1, "and 0 is", min2(in1))
    print("The minimum of", in1, "and", in2, "is", min2(in1, in2))

if __name__ == "__main__":
    main()
