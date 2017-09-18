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
        """ Test MISB 0601 Tag 1: Checksum Conversion."""

        # See MISB ST0902.5
        interpretation = "AA 43"
        tlv_hex_bytes = hexstr_to_bytes("01 02 AA 43")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import Checksum
        self.assertEqual(str(Checksum(value).value), interpretation)
        self.assertEqual(bytes(Checksum(value)), tlv_hex_bytes)

    def test_precisiontimestamp(self):
        """Test MISB 0601 Tag 2: Precision Timestamp Conversion."""

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
        """Test MISB 0601 Tag 3: Mission ID Conversion."""

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
        """Test MISB 0601 Tag 4: Platform Tail Number Conversion."""

        # See MISB ST0601.9
        interpretation = "AF-101"
        tlv_hex_bytes = hexstr_to_bytes("04 06 41 46 2D 31 30 31")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformTailNumber
        self.assertEqual(str(PlatformTailNumber(value).value), interpretation)
        self.assertEqual(bytes(PlatformTailNumber(value)), tlv_hex_bytes)

    def test_PlatformHeadingAngle(self):
        """Test MISB 0601 Tag 5: Platform Heading Angle Conversion."""

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
        """Test MISB 0601 Tag 6: Platform Pitch Angle Conversion."""

        # @TODO: Limit display precision and add units as per example.
        interpretation = "-0.4315317239905987"
        tlv_hex_bytes = hexstr_to_bytes("06 02 FD 3D")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformPitchAngle
        self.assertEqual(str(PlatformPitchAngle(value).value), interpretation)
        self.assertEqual(bytes(PlatformPitchAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(PlatformPitchAngle(value).value), -0.4315, 4)

    def test_PlatformRollAngle(self):
        """Test MISB 0601 Tag 7: Platform Roll Angle Conversion."""

        interpretation = "3.4058656575212893"
        tlv_hex_bytes = hexstr_to_bytes("07 02 08 B8")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformRollAngle
        self.assertEqual(str(PlatformRollAngle(value).value), interpretation)
        self.assertEqual(bytes(PlatformRollAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(PlatformRollAngle(value).value), 3.406, 3)

    # def test_PlatformTrueAirspeed(self):
    #     """MISB 0601 Tag 8: Platform True Airspeed Conversion."""
    #     pass

    # def test_PlatformIndicatedAirspeed(self):
    #     """MISB 0601 Tag 9: Platform Indicated Airspeed Conversion."""
    #     pass

    def test_PlatformDesignation(self):
        """MISB 0601 Tag 10: Platform Designation Conversion."""

        interpretation = "Predator"
        tlv_hex_bytes = hexstr_to_bytes("0A 08 50 72 65 64 61 74 6F 72")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import PlatformDesignation
        self.assertEqual(str(PlatformDesignation(value).value), interpretation)
        self.assertEqual(bytes(PlatformDesignation(value)), tlv_hex_bytes)

    def test_ImageSourceSensor(self):
        """MISB 0601 Tag 11: Image Source Sensor Conversion."""

        interpretation = "EO Nose"
        tlv_hex_bytes = hexstr_to_bytes("0B 07 45 4F 20 4E 6F 73 65")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import ImageSourceSensor
        self.assertEqual(str(ImageSourceSensor(value).value), interpretation)
        self.assertEqual(bytes(ImageSourceSensor(value)), tlv_hex_bytes)

    def test_ImageCoordinateSystem(self):
        """MISB 0601 Tag 12: Image Coordinate System Conversion."""

        interpretation = "Geodetic WGS84"
        tlv_hex_bytes = hexstr_to_bytes("0C 0E 47 65 6F 64 65 74 69 63 20 57 47 53 38 34")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import ImageCoordinateSystem
        self.assertEqual(str(ImageCoordinateSystem(value).value), interpretation)
        self.assertEqual(bytes(ImageCoordinateSystem(value)), tlv_hex_bytes)

    def test_SensorLatitude(self):
        """MISB 0601 Tag 13: Sensor Latitude Conversion."""

        interpretation = "60.176822966978335"
        tlv_hex_bytes = hexstr_to_bytes("0D 04 55 95 B6 6D")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorLatitude
        self.assertEqual(str(SensorLatitude(value).value), interpretation)
        self.assertEqual(bytes(SensorLatitude(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorLatitude(value).value), 60.17682297, 8)

    def test_SensorLongitude(self):
        """MISB 0601 Tag 14: Sensor Longitude Conversion."""

        interpretation = "128.42675904204452"
        tlv_hex_bytes = hexstr_to_bytes("0E 04 5B 53 60 C4")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorLongitude
        self.assertEqual(str(SensorLongitude(value).value), interpretation)
        self.assertEqual(bytes(SensorLongitude(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorLongitude(value).value), 128.42675904, 8)

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

    def test_SensorHorizontalFieldOfView(self):
        """MISB ST0601 Tag 16: Sensor Horizontal Field of View Conversion."""

        interpretation = "144.5712977798123"
        # Test data pulled from MISB ST0902.6 Annex C
        tlv_hex_bytes = hexstr_to_bytes("10 02 CD 9C")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorHorizontalFieldOfView
        self.assertEqual(str(SensorHorizontalFieldOfView(value).value), interpretation)
        self.assertEqual(bytes(SensorHorizontalFieldOfView(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorHorizontalFieldOfView(value).value), 144.571, 3)


    def test_SensorVerticalFieldOfView(self):
        """MISB ST0601 Tag 17: Sensor Vertical Field of View Conversion."""

        interpretation = "152.64362554360267"
        # Test data pulled from MISB ST0902.6 Annex C
        tlv_hex_bytes = hexstr_to_bytes("11 02 D9 17")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorVerticalFieldOfView
        self.assertEqual(str(SensorVerticalFieldOfView(value).value), interpretation)
        self.assertEqual(bytes(SensorVerticalFieldOfView(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorVerticalFieldOfView(value).value), 152.644, 3)


    def test_SensorRelativeAzimuthAngle(self):
        """MISB 0601 Tag 18: Sensor Relative Azimuth Ange Conversion."""

        interpretation = "160.71921143697557"
        # Test data pulled from MISB ST0902.6 Annex C

        tlv_hex_bytes = hexstr_to_bytes("12 04 72 4A 0A 20")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorRelativeAzimuthAngle
        self.assertEqual(str(SensorRelativeAzimuthAngle(value).value), interpretation)
        self.assertEqual(bytes(SensorRelativeAzimuthAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorRelativeAzimuthAngle(value).value), 160.71921144, 8)


    # def test_SensorRelativeElevationAngle(self):
    #     """MISB 0601 Tag 19: Sensor Relative Elevation Angle Conversion."""

    #     interpretation = "-168.79232483"
    #     # Test data pulled from MISB ST0902.6 Annex C
    #     tlv_hex_bytes = hexstr_to_bytes("13 04 87 F8 4B 86")
    #     value = tlv_hex_bytes[2:]

    #     from klvdata.misb0601 import SensorRelativeAzimuthAngle
    #     self.assertEqual(str(SensorRelativeAzimuthAngle(value).value), interpretation)
    #     self.assertEqual(bytes(SensorRelativeAzimuthAngle(value)), tlv_hex_bytes)
    #     self.assertAlmostEqual(float(SensorRelativeAzimuthAngle(value).value), -168.79232483, 8)


    def test_SensorRelativeRollAngle(self):
        """MISB 0601 Tag 20: Sensor Relative Roll Angle Conversion."""

        interpretation = "176.86543764939194"
        tlv_hex_bytes = hexstr_to_bytes("14 04 7D C5 5E CE")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SensorRelativeRollAngle
        self.assertEqual(str(SensorRelativeRollAngle(value).value), interpretation)
        self.assertEqual(bytes(SensorRelativeRollAngle(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SensorRelativeRollAngle(value).value), 176.86543765, 8)


    def test_SlantRange(self):
        """MISB 0601 Tag 21: Slant Range Conversion."""

        interpretation = "68590.98329874477"
        tlv_hex_bytes = hexstr_to_bytes("15 04 03 83 09 26")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import SlantRange
        self.assertEqual(str(SlantRange(value).value), interpretation)
        self.assertEqual(bytes(SlantRange(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(SlantRange(value).value), 68590.983, 3)


    def test_TargetWidth(self):
        """MISB 0601 Tag 22: Target Width Conversion."""

        interpretation = "722.8198672465096"
        tlv_hex_bytes = hexstr_to_bytes("16 02 12 81")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import TargetWidth
        self.assertEqual(str(TargetWidth(value).value), interpretation)
        self.assertEqual(bytes(TargetWidth(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(TargetWidth(value).value), 722.8, 1)


    def test_FrameCenterLatitude(self):
        """MISB 0601 Tag 23: Frame Center Latitude Conversion."""

        interpretation = "-10.542388633146132"
        tlv_hex_bytes = hexstr_to_bytes("17 04 F1 01 A2 29")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import FrameCenterLatitude
        self.assertEqual(str(FrameCenterLatitude(value).value), interpretation)
        self.assertEqual(bytes(FrameCenterLatitude(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(FrameCenterLatitude(value).value), -10.54238863, 8)


    def test_FrameCenterLongitude(self):
        """MISB 0601 Tag 24: Frame Center Longitude Conversion."""

        interpretation = "29.15789012292302"
        tlv_hex_bytes = hexstr_to_bytes("18 04 14 BC 08 2B")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import FrameCenterLongitude
        self.assertEqual(str(FrameCenterLongitude(value).value), interpretation)
        self.assertEqual(bytes(FrameCenterLongitude(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(FrameCenterLongitude(value).value), 29.15789012, 8)


    def test_FrameCenterElevation(self):
        """MISB 0601 Tag 25: Frame Center Elevation Conversion."""

        interpretation = "3216.0372320134275"
        tlv_hex_bytes = hexstr_to_bytes("19 02 34 F3")
        value = tlv_hex_bytes[2:]

        from klvdata.misb0601 import FrameCenterElevation
        self.assertEqual(str(FrameCenterElevation(value).value), interpretation)
        self.assertEqual(bytes(FrameCenterElevation(value)), tlv_hex_bytes)
        self.assertAlmostEqual(float(FrameCenterElevation(value).value), 3216.0, 1)

if __name__ == '__main__':
    unittest.main()
