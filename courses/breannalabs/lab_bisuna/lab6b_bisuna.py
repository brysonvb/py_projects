"""
Lab 6b - Function that gets string and prints index of each character
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def print_string(in_string):
    """
    Function to print string, index and character at index
    paramemter: inString - input string
    return: none
    """
    j = 0
    if len(in_string) == 0:
        print("Empty string")
    for i in in_string:
        print(j,":",i)
        j += 1


def main():
    """ driver """
    in_string = input("Enter a string: ")
    print_string(in_string)


if __name__ == "__main__":
    main()
