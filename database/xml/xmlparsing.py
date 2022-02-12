#!/usr/bin/env python

from xml.dom.minidom import parse, parseString

fn = "smiley.svg"

def parsexml():
    document = parse(fn)
    with open(fn) as file:
        document = parse(file)
    print(document.doctype)
    dtd = document.doctype
    print(dtd.entities["custom_entity"].childNodes)
    print()


def main():
    parsexml()


if __name__ == '__main__':
    main()
