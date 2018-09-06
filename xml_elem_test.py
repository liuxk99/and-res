# !/usr/bin/env python
# encoding=utf-8

import unittest

import xml_elem


class TestXmlEditor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test001(self):
        attr1 = xml_elem.Attr("name1", "value1")
        attr2 = xml_elem.Attr("name2", "value2")
        attrs = [attr1, attr2]
        elem = xml_elem.Element("Elem-1", attrs)

        print elem
        pass

if __name__ == '__main__':
    unittest.main()
