"""
Lab 11 - Function to Read and Write files, passing filename
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def write_file(filename):
    """
    Function to write into file
    paramemter: filename
    return: create file with name, major, and favorite hobby
    """
    with open(filename, "w", encoding="latin-1") as myfile:
        myfile.write("Breanna Bisuna\n")
        myfile.write("Computer Science\n")
        myfile.write("Playing Sports\n")
        myfile.close()


def read_file(filename):
    """
    Function to read file and print contents on screen
    paramemter: filename
    return: none
    """
    with open(filename, "r", encoding="latin-1") as myfile:
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
