from unittest import TestCase
import utils


class TestDumpHex(TestCase):
    def test_dumpHex(self):

        utils.dumpHex(32)
        print int("0x20", 16)

        x = 0x010302d1
        utils.dumpHex(x)

        pkg_id = x & 0xff000000
        utils.dumpHex(pkg_id)

        pkg_id >>= 24
        utils.dumpHex(pkg_id)

        print "change id from 0x01 to 0x03"
        utils.dumpHex(x)

        _id = 0x03 << 24
        new_id = (x & 0x00ffffff) + (0x03 << 24)
        utils.dumpHex(new_id)

    def test001(self):
        print "0x%08x" % 6557
        pass
    pass
