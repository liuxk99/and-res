# !/usr/bin/env python
# encoding=utf-8
import os


class Attr:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def __str__(self):
        res = "%s, %s" % (self._name, self._value)
        return res

    pass


class Element:
    def __init__(self, tagName, attrs):
        self._tagName = tagName
        self._attrs = attrs

    def append(self, attr):
        self._attrs.append(attr)

    def __str__(self):
        res = "{tagName = %s" % self._tagName + os.linesep
        res += "[" + os.linesep
        for attr in self._attrs:
            res += str(attr) + os.linesep
        res += "]" + os.linesep
        return res

    pass
