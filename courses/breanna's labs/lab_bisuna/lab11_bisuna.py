"""
Lab 11 - Function to Read and Write files, passing filename
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def write_file(fn):
    """
    Function to write into file
    paramemter: filename
    return: create file with name, major, and favorite hobby
    """
    myFile = open(fn, "w")
    myFile.write("Breanna Bisuna\n")
    myFile.write("Computer Science\n")
    myFile.write("Playing Sports\n")
    myFile.close()


def read_file(fn):
    """
    Function to read file and print contents on screen
    paramemter: filename
    return: none
    """
    myFile = open(fn, "r")
    line = myFile.readline()
    while line != "":
        print(line, end="")
        line = myFile.readline()
    myFile.close()


def main():
    write_file("lab11.txt")
    read_file("lab11.txt")


if __name__ == "__main__":
    main()
    
