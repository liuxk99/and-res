from unittest import TestCase

from res import Res

res = Res('anim', 'close_enter_left_to_right')


class TestRes(TestCase):
    def test_to_xml_def(self):
        print res.to_xml_def()
        # self.fail()

    def test_to_java(self):
        print res.to_java()
        # self.fail()

    def test_to_xml_ref(self):
        print res.to_xml_ref()
        # self.fail()

    def test_from_text(self):
        res.from_text("color.dialog_full_bg")
        print res
        print res.to_java()