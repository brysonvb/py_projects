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
    myfile = open(fn, "w", encoding="latin-1")
    myfile.write("Breanna Bisuna\n")
    myfile.write("Computer Science\n")
    myfile.write("Playing Sports\n")
    myfile.close()


def read_file(fn):
    """
    Function to read file and print contents on screen
    paramemter: filename
    return: none
    """
    myfile = open(fn, "r", encoding="latin-1")
    line = myfile.readline()
    while line != "":
        print(line, end="")
        line = myfile.readline()
    myfile.close()


def main():
    """ driver """
    write_file("lab11.txt")
    read_file("lab11.txt")


if __name__ == "__main__":
    main()
