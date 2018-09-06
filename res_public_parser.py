#!/usr/bin/env python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        public parser
# Purpose:
#
# Author:      thomas
#
# Created:     24/07/2016
# Copyright:   (c) thomas 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import sys

import dom_utils
import pxdom as my_dom
import res_public
import utils

ATTR_TAG_TYPE = "type"
ATTR_TAG_NAME = "name"
ATTR_TAG_ID = "id"

public_seq = []
pubs_to_append = []
elements_to_append = []


def parse_public_elem(elem):
    res_type = None
    res_name = None
    res_id = None
    if elem.hasAttributes:
        res_type = elem.getAttribute(ATTR_TAG_TYPE)
        res_name = elem.getAttribute(ATTR_TAG_NAME)
        res_id = elem.getAttribute(ATTR_TAG_ID)

    return res_public.Public(res_type, res_name, res_id)


def parse_element(elem):
    global public_seq
    if elem.tagName == 'public':
        pub = parse_public_elem(elem)
        public_seq.append(pub)
    pass


def proc_node(node):
    if node.nodeName == "resources":
        for e in elements_to_append:
            print "append %s" % e
            newNode = node.appendChild(e)
            print newNode

    if node.nodeType == node.ELEMENT_NODE:
        parse_element(node)
        pass
    pass


# node tree
def traverse(node):
    proc_node(node)
    if node.hasChildNodes:
        for child in node.childNodes:
            traverse(child)
    pass


def parse(infile):
    dom = my_dom.parse(infile)
    root = dom.documentElement
    traverse(root)
    pass


def edit(infile, outfile):
    print "edit(%s, %s)" % (infile, outfile)

    dom = my_dom.parse(infile)
    root = dom.documentElement

    global elements_to_append
    if len(pubs_to_append) > 0:
        for pub in pubs_to_append:
            print pub
            elem = dom.createElement("public")
            elem.setAttribute(ATTR_TAG_TYPE, pub._type)
            elem.setAttribute(ATTR_TAG_NAME, pub._name)
            if pub._id:
                elem.setAttribute(ATTR_TAG_ID, pub._get_id())

            elements_to_append.append(elem)

    traverse(root)
    if outfile:
        dom_utils.write(dom, outfile, False)

    elements_to_append = []
    pass


def parse_dir(res_dir):
    in_file = res_dir + "/res/values/public.xml"
    parse(in_file)
    pass


def append_public(res_file, pubs):
    global pubs_to_append
    pubs_to_append = pubs

    edit(res_file, res_file)

    pubs_to_append = []
    pass


def main(orig_args):
    if len(orig_args) > 0:
        res_file = orig_args[0]
        parse(res_file)
        utils.dump_seq1(public_seq)
    else:
        print "$1 is public file<public.xml>"

    pass


if __name__ == '__main__':
    main(sys.argv[1:])


def to_java(package):
    print "to_java() {"
    for pub in public_seq:
        print "  " + pub.to_java(package)
    print "}"
    pass


def to_xml():
    print "to_xml() {"
    for pub in public_seq:
        print "  " + pub.to_xml()
    print "}"

    pass


def to_res_ref(package):
    print "to_java() {"
    for pub in public_seq:
        print "  " + pub.to_ref(res_public.gModifier, package)
    print "}"
    pass
