import os
from unittest import TestCase

import res_public_parser
import test_const


class TestResPublicParser(TestCase):
    def test_parse(self):
        path = r"/home/thomas/Programmer/SDE/Android/letv/demeter/frameworks/base/core/res/res/values"
        path = r"C:\Users\thomas.XancL-NB\Desktop\and-res"
        xml_file = r"public.xml"

        res_public_parser.parse(path + os.path.sep + xml_file)
        # utils.dumpSeq1(res_public_parser.publicList)

        for pub in res_public_parser.public_seq:
            if pub._type == "drawable":
                print pub

        # res_public_parser.to_java(test_const.AndPackage)
        # res_public_parser.to_xml()
        # res_public_parser.to_res_ref(test_const.AndPackage)

        pass
