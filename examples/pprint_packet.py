#!/usr/bin/env python

import klvdata
import klvdata.common

if __name__ == "__main__":
    """ Returns single MISB0601 UAS Local Metadata Set Packet

    Stream Parser starts by assuming a key length, by default 16 bytes.

    Stream Parser looks up the 16 byte key and looks through its registered
    parsers for a match. If a match is found an aware parser is returned.

    Because this is a contrived example, packet is known to be of
    <class 'klvdata.misb0601.UASLocalMetadataSet'>.

    The "glue" or hard to see part of the schema is that the UAS LS parser
    inherits from SetParser. The Stream Parser is an iter object, so is the
    SetParser. Set Parser is also used for nested sets like Security LS. In a
    couple of ways StreamParser and Set Parser are very similar.

    The individual tags of the UAS LS are parsed much like the higher level.
    If one explores the MISB0601 module, each tag has a registered parser.

    Each parser inherits from a base parser class since there are relatively
    few parser/conversion types needed to interpet all values of the local set.

            # StringElementParser
            # BytesElementParser
            # DateTimeElementParser
            # MappedElementParser
            ## bytes_to_float(value, _domain, _range)

    The base parser class provides the interfaces that enables the objects to
    be manipualted as bytes, strings or numerics.

    This is all rather abstract, how about some examples?

    ! Likely a problem in MISB 0601 Tag #15 Sensor True Altitude. Got
    -5709.5108 but expected 14190.7.expected. Odd though, Tag 25 "Frame Center
    Elevation" appears to have same values and calculations. Is there perhaps
    an error in the document?

    """


def do_some_exercises():
    with open('./data/DynamicConstantMISMMSPacketData.bin', 'rb') as f:
        for packet in klvdata.StreamParser(f):
            # packet.structure()
            pass

    # The packet should still be available at this point... Let's take a look.

    # Want a timestamp?
    # print(packet[[2]])

    # What about name for timestamp?
    # print(packet[[2]].name)

    # What about displaying all the tags types?
    # print_all(packet, element_types)

    # What about displaying all the tags names?
    # print_all(packet, element_names)

    # What about displaying all the tags values?
    # print_all(packet, element_value)

    # What about displaying all the tags names and values?
    print_all(packet, element_full)


def print_all(outer_set, func, level=1, indent='    '):
    out = []

    def get_each_item_of(a_set, level=0):
        for item in a_set:
            out.append(level * indent + str(func(item)))

            if hasattr(item, 'items'):
                next_level = level + 1
                get_each_item_of(item.items.values(), next_level)

    get_each_item_of([outer_set, ], level)

    print('\n'.join([item for item in out]))


def element_types(item):
    return type(item)


def element_names(item):
    return item.name


def element_value(item):
    return item.value


def element_full(item):
    if len(item) > 1:
        key = klvdata.common.bytes_to_hexstr(item.key)
    else:
        key = klvdata.common.bytes_to_int(item.key)

    name = '{} ({}):'.format(item.name, key)

    if hasattr(item, 'items'):
        # value = ' ' * 4 + '---'
        value = '-' * 30
    elif hasattr(item.value, 'units'):
        value = '{} {}'.format(item.value, item.value.units)
    else:
        value = '{}'.format(item.value)

    return '{:<35} {}'.format(name, value)


if __name__ == '__main__':
    do_some_exercises()
