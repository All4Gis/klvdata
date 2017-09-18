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
# SOFTWARE.

from klvdata.common import hexstr_to_bytes
from klvdata.element import UnknownElement
from klvdata.elementparser import IntElementParser
from klvdata.elementparser import BytesElementParser
from klvdata.elementparser import DateTimeElementParser
from klvdata.elementparser import MappedElementParser
from klvdata.elementparser import StringElementParser
from klvdata.setparser import SetParser
from klvdata.streamparser import StreamParser


class UnknownElement(UnknownElement):
    pass


@StreamParser.add_parser
class UASLocalMetadataSet(SetParser):
    """MISB ST0601 UAS Local Metadata Set
    """
    key = hexstr_to_bytes('06 0E 2B 34 - 02 0B 01 01 – 0E 01 03 01 - 01 00 00 00')
    name = 'UAS Datalink Local Set'

    parsers = {}

    _unknown_element = UnknownElement



@UASLocalMetadataSet.add_parser
class Checksum(BytesElementParser):
    """Checksum used to detect errors within a UAV Local Set packet.

    Checksum formed as lower 16-bits of summation performed on entire
    LS packet, including 16-byte US key and 1-byte checksum length.

    Initialized from bytes value as BytesValue.
    """
    key = b'\x01'


@UASLocalMetadataSet.add_parser
class PrecisionTimeStamp(DateTimeElementParser):
    """Precision Timestamp represented in microseconds.

    Precision Timestamp represented in the number of microseconds elapsed
    since midnight (00:00:00), January 1, 1970 not including leap seconds.

    See MISB ST 0603 for additional details.
    """
    key = b'\x02'


@UASLocalMetadataSet.add_parser
class MissionID(StringElementParser):
    """Mission ID is the descriptive mission identifier.

    Mission ID value field free text with maximum of 127 characters
    describing the event.
    """
    key = b'\x03'


@UASLocalMetadataSet.add_parser
class PlatformTailNumber(StringElementParser):
    key = b'\x04'


@UASLocalMetadataSet.add_parser
class PlatformHeadingAngle(MappedElementParser):
    key = b'\x05'
    _domain = (0, 2**16-1)
    _range = (0, 360)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class PlatformPitchAngle(MappedElementParser):
    key = b'\x06'
    _domain = (-(2**15-1), 2**15-1)
    _range = (-20, 20)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class PlatformRollAngle(MappedElementParser):
    key = b'\x07'
    _domain = (-(2**15-1), 2**15-1)
    _range = (-50, 50)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class PlatformTrueAirspeed(MappedElementParser):
    key = b'\x08'
    _domain = (0, 2**8-1)
    _range = (0, 255)
    # units = 'meters/second'


@UASLocalMetadataSet.add_parser
class PlatformIndicatedAirspeed(MappedElementParser):
    key = b'\x09'
    _domain = (0, 2**8-1)
    _range = (0, 255)
    # units = 'meters/second'


@UASLocalMetadataSet.add_parser
class PlatformDesignation(StringElementParser):
    key = b'\x0A'
    # min_length, max_length = 0, 127


@UASLocalMetadataSet.add_parser
class ImageSourceSensor(StringElementParser):
    key = b'\x0B'
    # min_length, max_length = 0, 127


@UASLocalMetadataSet.add_parser
class ImageCoordinateSystem(StringElementParser):
    key = b'\x0C'
    # min_length, max_length = 0, 127


@UASLocalMetadataSet.add_parser
class SensorLatitude(MappedElementParser):
    key = b'\x0D'
    _domain = (-(2**31-1), 2**31-1)
    _range = (-90, 90)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorLongitude(MappedElementParser):
    key = b'\x0E'
    _domain = (-(2**31-1), 2**31-1)
    _range = (-180, 180)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorTrueAltitude(MappedElementParser):
    """MISB ST0601 Tag 15: Sensor True Altitue Conversion."""
    key = b'\x0F'
    _domain = (0, 2**16-1)
    _range = (-900, +19e3)
    units = 'meters'


@UASLocalMetadataSet.add_parser
class SensorHorizontalFieldOfView(MappedElementParser):
    """MISB ST0601 Tag 16: Sensor Horizontal Field of View Conversion."""
    key = b'\x10'
    _domain = (0, 2**16-1)
    _range = (0, 180)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorVerticalFieldOfView(MappedElementParser):
    """MISB ST0601 Tag 17: Sensor Vertical Field of View Conversion."""
    key = b'\x11'
    _domain = (0, 2**16-1)
    _range = (0, 180)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorRelativeAzimuthAngle(MappedElementParser):
    """MISB 0601 Tag 18: Sensor Relative Azimuth Ange Conversion."""
    key = b'\x12'
    _domain = (0, 2**32-1)
    _range = (0, 360)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorRelativeElevationAngle(MappedElementParser):
    """MISB 0601 Tag 19: Sensor Relative Elevation Angle Conversion."""
    key = b'\x13'
    _domain = (-(2**31-1), 2**31-1)
    _range = (-180, 180)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SensorRelativeRollAngle(MappedElementParser):
    """MISB 0601 Tag 20: Sensor Relative Roll Angle Conversion."""
    key = b'\x14'
    _domain = (0, 2**32-1)
    _range = (0, 360)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class SlantRange(MappedElementParser):
    """MISB 0601 Tag 21: Slant Range Conversion."""
    key = b'\x15'
    _domain = (0, 2**32-1)
    _range = (0, +5e6)
    units = 'meters'


@UASLocalMetadataSet.add_parser
class TargetWidth(MappedElementParser):
    """MISB 0601 Tag 22: Target Width Conversion."""
    key = b'\x16'
    _domain = (0, 2**16-1)
    _range = (0, +10e3)
    units = 'meters'


@UASLocalMetadataSet.add_parser
class FrameCenterLatitude(MappedElementParser):
    """MISB 0601 Tag 23: Frame Center Latitude Conversion."""
    key = b'\x17'
    _domain = (-(2**31-1), 2**31-1)
    _range = (-90, 90)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class FrameCenterLongitude(MappedElementParser):
    """MISB 0601 Tag 24: Frame Center Longitude Conversion."""
    key = b'\x18'
    _domain = (-(2**31-1), 2**31-1)
    _range = (-180, 180)
    units = 'degrees'


@UASLocalMetadataSet.add_parser
class FrameCenterElevation(MappedElementParser):
    """MISB 0601 Tag 25: Frame Center Elevation Conversion."""
    key = b'\x19'
    _domain = (0, 2**16)
    _range = (-900, +19e3)
    units = 'meters'

# @ST0601.add_parser
# class OffsetCornerLatitudePoint1(MappedElementParser):
#     tag, name = 26, "Offset Corner Latitude Point 1"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLongitudePoint1(MappedElementParser):
#     tag, name = 27, "Offset Corner Longitude Point 1"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLatitudePoint2(MappedElementParser):
#     tag, name = 28, "Offset Corner Latitude Point 2"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLongitudePoint2(MappedElementParser):
#     tag, name = 29, "Offset Corner Longitude Point 2"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLatitudePoint3(MappedElementParser):
#     tag, name = 30, "Offset Corner Latitude Point 3"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLongitudePoint3(MappedElementParser):
#     tag, name = 31, "Offset Corner Longitude Point 3"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLatitudePoint4(MappedElementParser):
#     tag, name = 32, "Offset Corner Latitude Point 4"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# @ST0601.add_parser
# class OffsetCornerLongitudePoint4(MappedElementParser):
#     tag, name = 33, "Offset Corner Longitude Point 4"
#     min_value, max_value, units = -0.075, +0.075, 'degrees'
#     min_length, max_length, signed = 2, 2, True
#
#
# # Tags 34-39 "Atmospheric Conditions"
#
# @ST0601.add_parser
# class TargetLocationLatitude(MappedElementParser):
#     tag, name = 40, "Target Location latitude"
#     min_value, max_value, units = -90, +90, 'degrees'
#     min_length, max_length, signed = 4, 4, True
#
#
# @ST0601.add_parser
# class TargetLocationLongitude(MappedElementParser):
#     tag, name = 41, "Target Location Longitude"
#     min_value, max_value, units = -180, +180, 'degrees'
#     min_length, max_length, signed = 4, 4, True
#
#
# @ST0601.add_parser
# class TargetLocationElevation(MappedElementParser):
#     tag, name = 42, "Target Location Elevation"
#     min_value, max_value, units = -900, +19e3, "meters"
#     min_length, max_length, signed = 2, 2, False
#
#
# # Tags 43 - 46 "Target Information"
#
# # Tag 47 "Generic Flag"


@UASLocalMetadataSet.add_parser
class UASDatalinkLSVersion(IntElementParser):
    """MISB 0601 Tag 65: UAS Datalink LS Version Number Conversion."""
    key = b'\x41'
    _domain = (0, 2**8-1)
    _range = (0, 255)


@UASLocalMetadataSet.add_parser
class MIISCoreIdentifier(BytesElementParser):
    """MISB 0601 Tag 94: MIIS Core Identifier.

    Local set tag to include the ST1204 MIIS Core identifier binary value
    within ST0601. Use according to the rules and requirements defined in `MISB
    ST` 1204.

    .. _MISB ST: http://www.gwg.nga.mil/misb/st_pubs.html
    """
    key = b'\x5E'
    _domain = (0, 2**8-1)
    _range = (0, 255)
