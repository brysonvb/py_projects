#!/usr/bin/env python

from xml.dom.minidom import parse, parseString, Node
import xml.etree.ElementTree as ET

fn = "smiley.svg"

def set_id_attribute(parent, attribute_name = "id"):
    if parent.nodeType == Node.ELEMENT_NODE:
        if parent.hasAttribute(attribute_name):
            parent.setIdAttribute(attribute_name)
    for child in parent.childNodes:
        set_id_attribute(child, attribute_name)

def parsexml():
    document = parse(fn)
    with open(fn) as file:
        document = parse(file)
    print(document.doctype)
    dtd = document.doctype
    print(dtd.entities["custom_entity"].childNodes)
    print()


def main():
    document = parse(fn)
    set_id_attribute(document)
    print(document.getElementById("skin"))
    print(document.getElementsByTagName("ellipse"))
    tree = ET.parse(fn)
    root = tree.getroot()
    #ET.dump(tree)
    for elm in root.findall(""):
        print(elm.attrib)


if __name__ == '__main__':
    main()
