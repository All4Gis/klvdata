#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2017 Matthew Pare (paretech@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE

import unittest

from klvdata.common import hexstr_to_bytes


class ParserSingleShort(unittest.TestCase):
    def test_checksum(self):
        # See MISB ST0902.5
        interpretation = "AA 43"
        tlv_hex_bytes = hexstr_to_bytes("01 02 AA 43")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import Checksum
        self.assertEqual(str(Checksum(value).value), interpretation)
        self.assertEqual(bytes(Checksum(value)), tlv_hex_bytes)

    def test_precisiontimestamp(self):
        # See MISB ST0902.5
        interpretation = "2009-01-12 22:08:22+00:00"
        tlv_hex_bytes = hexstr_to_bytes("02 08 00 04 60 50 58 4E 01 80")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PrecisionTimeStamp
        self.assertEqual(str(PrecisionTimeStamp(value).value), interpretation)
        self.assertEqual(bytes(PrecisionTimeStamp(value)), tlv_hex_bytes)

        # See MISB ST0601.9
        interpretation = "2008-10-24 00:13:29.913000+00:00"
        tlv_hex_bytes = hexstr_to_bytes("02 08 00 04 59 F4 A6 AA 4A A8")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PrecisionTimeStamp
        self.assertEqual(str(PrecisionTimeStamp(value).value), interpretation)
        self.assertEqual(bytes(PrecisionTimeStamp(value)), tlv_hex_bytes)

    def test_MissionID(self):
        # See MISB ST0902.5
        interpretation = "Mission 12"
        tlv_hex_bytes = hexstr_to_bytes("03 0A 4D 69 73 73 69 6F 6E 20 31 32")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import MissionID
        self.assertEqual(str(MissionID(value).value), interpretation)
        self.assertEqual(bytes(MissionID(value)), tlv_hex_bytes)

        # See MISB ST0601.9
        interpretation = "MISSION01"
        tlv_hex_bytes = hexstr_to_bytes("03 09 4D 49 53 53 49 4F 4E 30 31]")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import MissionID
        self.assertEqual(str(MissionID(value).value), interpretation)
        self.assertEqual(bytes(MissionID(value)), tlv_hex_bytes)

    def test_PlatformTailNumber(self):
        # See MISB ST0601.9
        interpretation = "AF-101"
        tlv_hex_bytes = hexstr_to_bytes("04 06 41 46 2D 31 30 31")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformTailNumber
        self.assertEqual(str(PlatformTailNumber(value).value), interpretation)
        self.assertEqual(bytes(PlatformTailNumber(value)), tlv_hex_bytes)

    def test_PlatformHeadingAngle(self):

        # See MISB ST0601.9
        # @TODO: Limit display precision and add units as per example.
        interpretation = "159.97436484321355"
        tlv_hex_bytes = hexstr_to_bytes("05 02 71 C2")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformHeadingAngle
        self.assertEqual(str(PlatformHeadingAngle(value).value), interpretation)
        self.assertEqual(bytes(PlatformHeadingAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(PlatformHeadingAngle(value).value), 159.974, 3)

    def test_PlatformPitchAngle(self):
        """Test MISB ST0601 Tag 6 - Platform Pitch Angle Conversion."""
        # @TODO: Limit display precision and add units as per example.
        interpretation = "-0.4315317239905987"
        tlv_hex_bytes = hexstr_to_bytes("06 02 FD 3D")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformPitchAngle
        self.assertEqual(str(PlatformPitchAngle(value).value), interpretation)
        self.assertEqual(bytes(PlatformPitchAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(PlatformPitchAngle(value).value), -0.4315, 4)

    def test_PlatformRollAngle(self):
        """Test MISB ST0601 Tag 7 - Platform Roll Angle Conversion."""

        interpretation = "3.4058656575212893"
        tlv_hex_bytes = hexstr_to_bytes("07 02 08 B8")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformRollAngle
        self.assertEqual(str(PlatformRollAngle(value).value), interpretation)
        self.assertEqual(bytes(PlatformRollAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(PlatformRollAngle(value).value), 3.406, 3)

    def test_SensorTrueAltitude(self):
        """Test MISB ST0601 Tag 15: Sensor True Altitude Conversion"""

        interpretation = "14190.719462882427"
        # Test data pulled from MISB ST0902.6 Annex C
        tlv_hex_bytes = hexstr_to_bytes("0F 02 C2 21")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorTrueAltitude
        self.assertEqual(str(SensorTrueAltitude(value).value), interpretation)
        self.assertEqual(bytes(SensorTrueAltitude(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorTrueAltitude(value).value), 14190.7, 1)

if __name__ == '__main__':
    unittest.main()
