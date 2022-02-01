"""
Lab 9 - create an empty list and add elements, then get the sum and average.
Programmed by: Breanna Bisuna
Date: 8Nov2020
"""

def main():
    """ driver """
    mylist = []
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    sumlist = 0
    for i in mylist:
        print("List element",i)
        sumlist += i
    print("\nSum of items in list:",sumlist)
    print("Average of items in list:", sumlist/len(mylist))

if __name__ == "__main__":
    main()
