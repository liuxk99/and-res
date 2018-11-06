from unittest import TestCase

import res_color
import test_const
import res_public
import res_public_parser
import res_xml

sdk_res_dir = test_const.sdkResDir
and_res_dir = test_const.andResDir
eui_res_dir = test_const.euiResDir


class TestPublic(TestCase):

    def test001(self):
        # <color name="es_transparent">#00000000</color>
        # <color name="es_controller_progress_thumb">#e3e3e3</color>
        color = res_color.Color("es_transparent", '#00000000')
        print color.to_xml()

        color = res_color.Color("es_controller_progress_thumb", '#e3e3e3')
        print color.to_xml()
        pass

    pass
