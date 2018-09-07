# encoding=utf-8
import os
from unittest import TestCase

import res_public_parser
import test_const
import utils
import re

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

    def test_eui(self):
        path = r"/home/thomas/Programmer/SDE/Android/letv/demeter/frameworks/base/core/res/res/values"
        path = r"C:\Users\thomas.XancL-NB\Desktop"
        xml_file = r"public.xml"

        res_public_parser.parse(path + os.path.sep + xml_file)
        # utils.dumpSeq1(res_public_parser.publicList)

        overlay_file = r"overlay.xml"
        res_public_parser.parse(path + os.path.sep + overlay_file)
        public_seq = res_public_parser.public_seq[:]

        dict = {u'key':'value'}
        for pub in public_seq:
            has = dict.has_key(pub._type)
            if has:
                res_id = dict[pub._type]
                if pub._id > res_id:
                    dict[pub._type] = pub._id
            else:
                dict[pub._type] = pub._id

        print dict

        # res_public_parser.to_java(test_const.AndPackage)
        # res_public_parser.to_xml()
        # res_public_parser.to_res_ref(test_const.AndPackage)

        res_public_parser.public_seq = []

        eui_publc_xml_file = r"eui.public.xml"
        res_public_parser.parse(path + os.path.sep + eui_publc_xml_file)
        # utils.dumpSeq1(res_public_parser.publicList)

        id_dict = {}
        eui_public_seq = res_public_parser.public_seq
        for pub in eui_public_seq:
            old = pub._id
            res_id = dict[pub._type]
            pub._id = res_id + 1
            dict[pub._type] = pub._id
            new = pub._id
            id_dict[pub._name] = "0x%08x" % new

            # print('s/id="0x%08x"/id="0x%08x"/g' % (old, new))

        for key in id_dict:
            print("%s : %s" % (key, id_dict[key]))

        # res_public_parser.to_xml()
        target_xml_file = "target.xml"

        with open(path + os.path.sep + target_xml_file, 'w') as out_file:
            with open(path + os.path.sep + eui_publc_xml_file) as in_file:
                for line in in_file:
                    new_line = line
                    for name in id_dict.keys():
                        # 定位到需要替换的行。
                        if line.find('"%s"' % name) >= 0:
                            new_line = re.sub(r'id="0x[0-9a-zA-Z]+"', 'id="%s"' % id_dict[name], line)
                            break
                    out_file.write(new_line)

        pass
