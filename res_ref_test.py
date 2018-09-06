#!/usr/bin/env python
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
import unittest
import res_ref as MyResRef


class ResRefTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGen01(self):
        ref = MyResRef.ResRef()
        ref.init(u"@", u"android", u"drawable", u"letv_shutdown_logo")
        # self.assertEqual(ref.__str__(), u"@android:drawable/letv_shutdown_logo", u"test str()")
        pass

    def testGen02(self):
        ref = MyResRef.ResRef();
        ref.parse(u"?attr/textAppearance", u"android")

        ExpRet = MyResRef.ResRef();
        ExpRet.init(u"?", u"android", u"attr", u"textAppearance")

        # self.assertEqual(ref, ExpRet, u"test init01, init02")
        pass

    def testGen03(self):
        ref = MyResRef.ResRef()
        ref.parse(u"32sp", u"android")
        print ref

        ExpRet = MyResRef.ResRef()
        ExpRet.init(u"?", u"android", u"attr", u"textAppearance")

        # self.assertNotEqual(ref, ExpRet, u"test init01, init02")
        pass

    def testcase_004(self):
        ref = MyResRef.ResRef()
        ref.parse("@interpolator/decelerate_quad", "android")
        print ref.to_xml_str()
        pass

    pass

    def testProcJava(self):
        src = MyResRef.ResRef()
        src.parse("@android:drawable/scrollbar_handle_letv", "android")

        dst = MyResRef.ResRef()
        dst.parse("@eui:drawable/scrollbar_handle_letv", "eui")

        javaFile = r""

        pass

    def test_to_java_str(self):
        src = MyResRef.ResRef()
        src.parse("@android:drawable/scrollbar_handle_letv", "android")

        exp_res = "com.android.internal.R.drawable.scrollbar_handle_letv"
        self.assertEqual(src.to_java_str(), exp_res)
        pass


if __name__ == '__main__':
    unittest.main()
