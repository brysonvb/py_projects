"""
Lab 9 - create an empty list and add elements, then get the sum and average.
Programmed by: Breanna Bisuna
Date: 8Nov2020
"""

def main():
    """ driver """
    myList = []
    myList.append(1)
    myList.append(2)
    myList.append(3)
    sumList = 0
    for i in myList:
        print("List element",i)
        sumList += i
    print("\nSum of items in list:",sumList)
    print("Average of items in list:", sumList/len(myList))

if __name__ == "__main__":
    main()
