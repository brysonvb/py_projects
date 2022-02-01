"""
Lab 6b - Function that gets string and prints index of each character
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def printString(inString):
    """
    Function to print string, index and character at index
    paramemter: inString - input string
    return: none
    """
    j = 0
    if len(inString) == 0:
        print("Empty string")
    for i in inString:
        print(j,":",i)
        j += 1


def main():
    inString = input("Enter a string: ")
    printString(inString)


if __name__ == "__main__":
    main()
