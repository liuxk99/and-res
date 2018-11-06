#!/usr/bin/env python
# encoding=utf-8
import res_ref

gModifier = "@"


class Color:
    def __init__(self, _name, _value):
        self._name = _name
        self._value = _value
        if isinstance(_value, basestring):
            if len(_value) > 0:
                idx = _value.index('#')
                self._aRgb = int(_value[idx + 1:], 16)
            else:
                self._aRgb = None
        pass

    def __str__(self):
        if self._aRgb:
            return 'color {name: %s, rgb: 0x%08x}' % (self._name, self._aRgb)
        else:
            return 'color {name: %s, value: 0x%08x}' % (self._name, self._value)

    def to_xml(self):
        if self._aRgb:
            return '<color name="%s">#%08x</color>' % (self._name, self._aRgb)
        else:
            return '<color name="%s">%s</color>' % (self._name, self._value)

    def to_java(self, package):
        return "%s.R.%s.%s" % (package, 'color', self._name)

    def to_ref(self, modifier, package):
        ref = self.gen(modifier, package)
        return str(ref)

    pass

    def gen(self, modifier, package):
        ref = res_ref.ResRef()
        ref.init(modifier, package, 'color', self._name)
        ref.set_access(res_ref.ACCESS_PUBLIC)
        return ref
