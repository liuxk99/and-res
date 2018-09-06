#!/usr/bin/env python
# encoding: utf-8
# -------------------------------------------------------------------------------
# Name:        resource reference
# Purpose:     class for android resource references

#
# Author:      thomas
#
# Created:     17/06/2016
# Copyright:   (c) thomas 2016
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import re

import xml_elem

PACKAGE_PATTERN = r"[\.a-zA-Z0-9]+"
TYPE_PATTERN = r"[a-z]+"
ID_PATTERN = r"[^/]+"
MODIFIER_PAT1 = r"[\@\?]?[\*\+]?"
MODIFIER_PAT2 = r"[\@\?]?[\+]?"

VALUE_ATTR_PATTERN1 = r'[\?\@](%s):attr/(%s)' % (PACKAGE_PATTERN, ID_PATTERN)
VALUE_ATTR_PATTERN2 = r'\?attr/(%s)' % PACKAGE_PATTERN

NAME_ATTR_PATTERN1 = r'\@?(%s):(%s)' % (PACKAGE_PATTERN, ID_PATTERN)
NAME_ATTR_PATTERN2 = r'(%s)' % ID_PATTERN

VALUE_PATTERN1 = r"(%s)(%s):(%s)/(%s)" % (MODIFIER_PAT1, PACKAGE_PATTERN, TYPE_PATTERN, ID_PATTERN)
VALUE_PATTERN2 = r"(%s)(%s)/(%s)" % (MODIFIER_PAT2, TYPE_PATTERN, ID_PATTERN)
VALUE_PATTERN3 = r"(%s)(%s):(%s)" % (MODIFIER_PAT1, PACKAGE_PATTERN, ID_PATTERN)
VALUE_PATTERN4 = r"\?(%s)" % ID_PATTERN

ATTR_MODIFIER = "?"

MODIFIER_ALL = "@*"
MODIFIER_PUBLIC = "@"

ACCESS_INTERNAL = 0
ACCESS_SYMBOL = 1
ACCESS_PUBLIC = 2


def parse_item_value(text):
    text = unicode(text)
    modifier = None
    package = None
    rtype = None
    name = text

    p1 = re.compile(unicode(VALUE_PATTERN1))
    m = p1.match(text)
    if m:
        modifier = m.group(1)
        package = m.group(2)
        rtype = m.group(3)
        name = m.group(4)
    else:
        p2 = re.compile(unicode(VALUE_PATTERN2))
        m = p2.match(text)
        if m:
            # print m.groups()
            modifier = m.group(1)
            rtype = m.group(2)
            name = m.group(3)
        else:
            p3 = re.compile(unicode(VALUE_PATTERN3))
            m = p3.match(text)
            if m:
                rtype = "attr"
                modifier = m.group(1)
                package = m.group(2)
                name = m.group(3)
            else:
                p4 = re.compile(unicode(VALUE_PATTERN4))
                m = p4.match(text)
                if m:
                    name = m.group(1)
                    rtype = "attr"

    return modifier, package, rtype, name


class ResRef:
    def __init__(self):
        self._package = None
        self._type = None
        self._name = None
        self._modifier = None
        self._access = ACCESS_INTERNAL
        pass

    def init(self, modifier, package, type, name):
        self._package = package
        self._type = type
        self._name = name
        self._modifier = modifier
        self._access = ACCESS_INTERNAL

    def __str__(self):
        modifier = self.access_to_modifier(self._access)
        return u"%d:%02s%s:%s/%s" % (self._access, modifier, self._package, self._type, unicode(self._name))

    def __eq__(self, other):
        if not isinstance(other, ResRef):
            raise TypeError, "can't cmp other type to ResRef!"
        # self._modifier == other._modifier and
        if self._package == other._package and self._type == other._type and self._name == other._name:
            return True
        else:
            return False

    def parse(self, text, def_package):
        m, p, t, n = parse_item_value(text)
        self._modifier = m
        if p is None:
            p = def_package

        self._package = p
        self._type = t
        self._name = n
        self._access = ACCESS_INTERNAL
        pass

    def replace(self, package):
        self._modifier = MODIFIER_ALL
        self._package = package
        pass

    pass

    def to_java_str(self):
        private = "com.%s.internal.R.%s.%s"
        public = "%s.R.%s.%s"

        java_format = private
        if self._access:
            java_format = public

        return java_format % (self._package, self._type, self._name)

    def to_xml_str(self, package=None):
        modifier = MODIFIER_ALL
        if self._access:
            modifier = MODIFIER_PUBLIC
        if package != self._package:
            return "%s%s:%s/%s" % (modifier, self._package, self._type, self._name)
        else:
            return "%s%s/%s" % (MODIFIER_PUBLIC, self._type, self._name)

    def to_symbol_element(self):
        tagName = "java-symbol"
        if self._access == ACCESS_PUBLIC:
            tagName = "public"
        attr_list = [xml_elem.Attr("name", self._name), xml_elem.Attr("type", self._type)]
        return xml_elem.Element(tagName, attr_list)

    def set_access(self, access):
        self._access = access
        self._modifier = self.access_to_modifier(access)
        pass

    def find_res(self, pubs):
        for pub in pubs:
            if self._type == pub._type and self._name == pub._name:
                return True
        return False

    def access_to_modifier(self, _access):
        if self._type == "attr":
            return ATTR_MODIFIER

        if _access == ACCESS_PUBLIC:
            return MODIFIER_PUBLIC

        return MODIFIER_ALL


def proc_java(src, dst, file):
    pass
