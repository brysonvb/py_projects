"""
Lab 10 - create 2 sets and get their intersection, union, difference, and symmetric difference
Programmed by: Breanna Bisuna
Date: 8Nov2020
"""

def main():
    """ driver """
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}

    print("Set 1:", set1)
    print("Set 2:", set2)

    # Intersection
    print("\nIntersection Set 1 & Set 2:")
    print(set1 & set2)

    # Union
    print("\nUnion Set 1 and Set 2:")
    print(set1 | set2)

    # Difference
    print("\nDifference Set 1 and Set 2:")
    print(set1 - set2)

    # Symmetric Difference
    print("\nSymmetric Difference Set 1 and Set 2:")
    print(set1 ^ set2)


if __name__ == "__main__":
    main()
