#!/usr/bin/env python
# encoding=utf-8


class Res:
    def __init__(self, _type, _name):
        self._type = _type
        self._name = _name
        pass

    def from_text(self, text):
        # anim.close_enter_left_to_right
        str_list = text.split('.')
        if len(str_list) == 2:
            self._type = str_list[0]
            self._name = str_list[1]

    def __str__(self):
        return '%s.%s' % (self._type, self._name)

    def to_xml_def(self):
        return 'name="%s"' % self._name

    def to_java(self):
        return "R.%s.%s" % (self._type, self._name)

    def to_xml_ref(self):
        return '@%s/%s' % (self._type, self._name)

    def __eq__(self, other):
        if self._type == other._type and self._name == other._name:
            return True
        return False

    pass
