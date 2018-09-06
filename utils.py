#!/usr/bin/env python
# encoding=utf-8
# -------------------------------------------------------------------------------
# Name:        utility
# Purpose:
#
# Author:      thomas
#
# Created:     23/06/2016
# Copyright:   (c) thomas 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import os


def dump_seq1(seq):
    print "seq:[%d]{" % len(seq)
    for e in seq:
        print unicode(e)
    print "}"
    pass


def dumpSeq(seq, eFile=None):
    if (eFile != None):
        print eFile

    print "seq: {"
    for e in seq:
        print e
    print "}"


def printTestCase(name):
    print "-------------------------------------"
    print "TestCase: '%s'" % name
    pass


def procId(id):
    res = id
    if id != None:
        res = (id & 0x00ffffff) + 0x03000000

    return res


def procId2(id):
    if id != None and len(id) > 0:
        x = int(id, 16)
        newId = (x & 0x00ffffff) + 0x03000000
        return newId
    else:
        return None
    pass


def hex2Str(x):
    if (x != None):
        return "0x%08x" % x

    return ""


def dumpHex(x):
    if (x != None):
        print "0x%08x" % x
    pass


def testcase01():
    dumpHex(32)
    print int("0x20", 16)

    x = 0x010302d1
    dumpHex(x)

    pkgId = x & 0xff000000
    dumpHex(pkgId)

    pkgId = pkgId >> 24
    dumpHex(pkgId)

    print "change id from 0x01 to 0x03"
    dumpHex(x)
    newId = (x & 0x00ffffff) + 0x03000000
    dumpHex(newId)

    pass


def testcase02():
    str = "0x010302d1"
    res = procId2(str)

    print '%s = procId2("%s")' % (hex2Str(res), str)

    str = ""
    res = procId2(str)
    print '%s = procId2("%s")' % (hex2Str(res), str)

    pass


def read_seq_from_file(file_name, seq):
    with open(file_name) as f:
        for line in f:
            if line not in seq:
                new_line = line.replace(os.linesep, '')
                seq.append(new_line)
    pass


def write_seq_into_file(file_name, seq):
    with open(file_name, "w") as f:
        for line in seq:
            f.write(line)
            f.write(os.linesep)

    pass


def main():
    seq = ["hello", "world"]
    dump_seq1(seq)

    # testcase01()
    testcase02()
    pass


if __name__ == '__main__':
    main()
