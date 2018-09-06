# !/usr/bin/env python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        xml_editor
# Purpose:
#
# Author:      thomas
#
# Created:     07/06/2016
# Copyright:   (c) thomas 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
"""xml_editor - xml editor for replace android resource with eui resource
"""

import urllib
import urlparse

import dom_utils
import pxdom as my_dom
import res_ref

__version__ = 1, 0
__author__ = 'Thomas Liu <liuxk99@gmail.com>'
__date__ = 2016, 6, 14
__all__ = ['edit']

elements_to_remove = []
elements_to_append = []
IN_TRANSFER = False
PACKAGE = None


def dump_element(elem):
    print "%s{" % elem.tagName

    if elem.hasAttributes:
        for i in range(elem.attributes.length):
            attr = elem.attributes.item(i)
            print '%s="%s"' % (attr.name, attr.value)
        pass

    print "}"

    pass


def transfer_element(elem):
    # print "%s{" % elem.tagName

    if elem.hasAttributes:
        for i in range(elem.attributes.length):
            attr = elem.attributes.item(i)
            value = attr.value

            if PACKAGE:
                ref = res_ref.ResRef()
                ref.parse(attr.value, PACKAGE)
                if ref._type:
                    newAttr = attr
                    newAttr.value = ref.to_xml_str()
                    elem.setAttributeNode(newAttr)
                    print '[REPLACED]%s="%s"->%s' % (attr.name, value, newAttr.value)
        pass

    # print "}"

    pass


def proc_element(elem):
    transfer_element(elem)

    parent = elem.parentNode

    for element in elements_to_remove:
        if element._tagName == elem.tagName:
            # dump_element(elem)

            matched = True
            for attr in element._attrs:
                value = elem.getAttribute(attr._name)
                if value and value == attr._value:
                    print attr
                else:
                    matched = False
                    break

            if matched:
                print "matched: %s" % str(element)
                parent.removeChild(elem)
                elements_to_remove.remove(element)
    pass


def proc_node(node):
    if node.nodeName == "resources":
        for e in elements_to_append:
            print e
            newNode = node.appendChild(e)
            print newNode

    if node.nodeType == node.ELEMENT_NODE:
        proc_element(node)
        pass
    pass


# node tree
def traverse(node):
    proc_node(node)
    if node.hasChildNodes:
        for child in node.childNodes:
            traverse(child)
    pass


def edit(infile, out_file):
    print "edit(%s)" % infile

    dom = my_dom.parse(infile)
    root = dom.documentElement
    traverse(root)
    if out_file:
        dom_utils.write(dom, out_file)
    pass


def remove(in_file, out_file, elements):
    print "remove(%s, %s)" % (in_file, out_file)
    global elements_to_remove
    elements_to_remove = elements

    dom = my_dom.parse(in_file)
    root = dom.documentElement
    traverse(root)
    if out_file:
        dom_utils.write(dom, out_file, False)

    elements_to_remove = []
    pass


def append(in_file, out_file, elements):
    print "append(%s, %s)" % (in_file, out_file)

    dom = my_dom.parse(in_file)
    root = dom.documentElement

    global elements_to_append
    elements_to_append = []

    if len(elements) > 0:
        for e in elements:
            e = dom.createElement(e.tag)
            elem.setAttribute(ATTR_TAG_TYPE, sym._type)
            elem.setAttribute(ATTR_TAG_NAME, sym._name)
            elements_to_append.append(elem)

    traverse(root)

    elements_to_append = []
    pass


def path2url(path):
    return urlparse.urljoin(
        'file:', urllib.pathname2url(path))


def transfer(in_file, out_file, package):
    global PACKAGE
    PACKAGE = package

    global IN_TRANSFER
    IN_TRANSFER = True

    dom = my_dom.parse(in_file)
    root = dom.documentElement
    traverse(root)
    if out_file:
        dom_utils.write(dom, out_file, True)

    IN_TRANSFER = False
    PACKAGE = None
    pass
