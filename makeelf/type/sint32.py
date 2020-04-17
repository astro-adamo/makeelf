#!/usr/bin/env python3
## \file sint32.py
#  \brief Signed 32-bit Integer
import struct

class sint32:

    def __init__(self, integer, little=False):
        self.little = little
        if little:
            self._endian = '<'
        else:
            self._endian = '>'
        self.integer = integer

    def __bytes__(self):
        return struct.pack("%si" % self._endian, int(self.integer))

    def __str__(self):
        return "%d" % self.integer

    def __len__(self):
        return len(bytes(self))

    def from_bytes(b, little=False):
        if little:
            _endian = '<'
        else:
            _endian = '>'
        integer, = struct.unpack("%si" % _endian, b[:4])
        return sint32(integer), b[4:]
