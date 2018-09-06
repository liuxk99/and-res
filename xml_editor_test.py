# !/usr/bin/env python
# encoding=utf-8

import unittest

import test_const
import xml_editor
import xml_elem

in_file = r"/home/thomas/Programmer/SDE/Android/letv/demeter/frameworks/base/core/res/res/values/public.xml"
out_file = r"/home/thomas/Programmer/SDE/Android/letv/demeter/frameworks/base/core/res/res/values/public1.xml"


class TestXmlEditor(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test001(self):
        xml_editor.edit("public.xml", None)
        pass

    def test002(self):
        xml_editor.edit(in_file, out_file)
        pass

    def test003(self):
        anim_attr_type = xml_elem.Attr("type", "anim")
        anim_attr_name1 = xml_elem.Attr("name", "close_enter_left_to_right")
        anim_attr_name2 = xml_elem.Attr("name", "close_exit_left_to_right")

        attrs1 = [anim_attr_type, anim_attr_name1]
        pub_elem1 = xml_elem.Element("public", attrs1)

        attrs2 = [anim_attr_type, anim_attr_name2]
        pub_elem2 = xml_elem.Element("public", attrs2)

        elements = [pub_elem1, pub_elem2]

        xml_editor.remove(in_file, out_file, elements)
        pass

    def testcase_004(self):
        xml_file = test_const.andResDir + "/res/anim/open_exit_close_enter_stick.xml"
        xml_editor.transfer(xml_file, xml_file, test_const.AndPackage)
        pass

if __name__ == '__main__':
    unittest.main()
