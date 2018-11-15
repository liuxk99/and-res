from unittest import TestCase

import res_names_parser
from res import Res


class TestParse_line(TestCase):
    def test_parse_line(self):
        res = Res("", "")
        res.from_text('color.letv_empty_message_color')

        line = '            android:textColor="@color/letv_empty_message_color"'
        m = res_names_parser.parse_line(res, line)
        self.assertIsNotNone(m)
        # self.fail()
