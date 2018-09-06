#!/usr/bin/env python
# encoding=utf-8
import res_ref

gModifier = "@"


class Public:
    def __init__(self, _type, _name, _id):
        self._type = _type
        self._name = _name
        if isinstance(_id, basestring):
            if len(_id) > 0:
                idx = int(_id, 16)
                self._id = idx
            else:
                self._id = None
        else:
            self._id = _id
        pass

    def __str__(self):
        if self._id:
            return 'public {type: %s, name: %s, id: 0x%08x}' % (self._type, self._name, self._id)
        else:
            return 'public {type: %s, name: %s}' % (self._type, self._name)

    def _get_id(self):
        if self._id:
            return "0x%08x" % self._id
        return None

    def replace_id(self, package_id):
        if self._id:
            self._id = (self._id & 0x00ffffff) + (package_id << 24)
        pass

    def id_to_str(self):
        if self._id:
            _id = self._id
            p = (0x01000000 & _id) >> 24
            t = (0x00ff0000 & _id) >> 16
            order = 0x0000ffff & _id
            return "package id: 0x%02x, type: 0x%02x, order no: 0x%04x" % (p, t, order)

        return "no id"

    def to_xml(self):
        if self._id:
            return '<public type="%s" name="%s" id="0x%08x"/>' % (self._type, self._name, self._id)
        else:
            return '<public type="%s" name="%s"/>' % (self._type, self._name)

    def to_java(self, package):
        return "%s.R.%s.%s" % (package, self._type, self._name)

    def to_ref(self, modifier, package):
        ref = self.gen(modifier, package)
        return str(ref)

    pass

    def gen(self, modifier, package):
        ref = res_ref.ResRef()
        ref.init(modifier, package, self._type, self._name)
        ref.set_access(res_ref.ACCESS_PUBLIC)
        return ref
