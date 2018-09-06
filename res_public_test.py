from unittest import TestCase

import test_const
import res_public
import res_public_parser
import res_xml

sdk_res_dir = test_const.sdkResDir
and_res_dir = test_const.andResDir
eui_res_dir = test_const.euiResDir


class TestPublic(TestCase):
    def test_replace_id(self):
        pub = res_public.Public("drawable", "xxx", 0x01090f01)
        print pub
        print pub.id_to_str()

        pub.replace_id(3)
        print pub
        print pub.id_to_str()

        pub1 = res_public.Public("drawable", "yyy", None)
        print pub1
        print pub1.id_to_str()

        pass

    def test002(self):
        pub = res_public.Public("drawable", "xxx", 0x01090f01)
        pub_deltas = [pub]

        pub_file = and_res_dir + res_xml.PUBLIC_FILE
        res_public_parser.append_public(pub_file, pub_deltas)

        pass

    pass
