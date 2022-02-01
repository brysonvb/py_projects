"""
Lab 8a - Partition the given string into 3 parts using a separator
Programmed by: Breanna Bisuna
Date: 10Nov2020
"""

def split_it_up(a_string, sep):
    """
    Function separates the given string using separator
    paramemter: a_string - string to split, sep - separator used as marker
    return: 3 tuple contins string before sep, sep, and string after sep
    """
    if len(sep) == 0: # can't process empty separator
        sep = " "
    lstring = ""
    rstring = ""
    ssep = ""
    mysep = False
    i = 0
    while i < len(a_string):
        if a_string[i] == sep[0] and mysep is not True:
            ssep = sep[0]
            for j in range(len(sep)-1):
                i += 1
                ssep += a_string[i+j]
            if ssep == sep:
                mysep = True
                i += 1
            continue
        if mysep:
            rstring += a_string[i]
        else:
            lstring += a_string[i]
        i += 1
    return (lstring, ssep, rstring)


def main():
    """ driver """
    print(split_it_up("hello world"," "))
    print(split_it_up("hello world","wo"))
    print(split_it_up("hello world","r"))
    print(split_it_up("hello world, I am ready to program"," "))
    print(split_it_up("hello world","|"))

if __name__ == "__main__":
    main()
