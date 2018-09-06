#!/usr/bin/env python
# encoding=utf-8
import pxdom as my_dom
import xml_editor


def write(dom, outfile, first_attr_newline=True):
    print "write(dom, %s, %d)" % (outfile, first_attr_newline)

    old = my_dom.first_attr_newline
    my_dom.first_attr_newline = first_attr_newline

    output = dom.implementation.createLSOutput()
    output.systemId = xml_editor.path2url(outfile)
    output.encoding = 'utf-8'
    serialiser = dom.implementation.createLSSerializer()
    serialiser.write(dom, output)
    my_dom.first_attr_newline = old
    pass


def genLevel0(dom):
    return dom.createTextNode("\n")


def genLevel1(dom):
    return dom.createTextNode("\n    ")


def genLevel2(dom):
    return dom.createTextNode("\n        ")