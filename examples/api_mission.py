from klvdata.misb0601 import MissionID
from klvdata import common

if __name__ == "__main__":
    # See MISB ST0601.9
    interpretation = "MISSION01"
    tlv_hex_bytes = common.hexstr_to_bytes("03 09 4D 49 53 53 49 4F 4E 30 31]")
    value = tlv_hex_bytes[2:]

    mission_id = MissionID(value)

    print("{} = {}".format(mission_id.name, mission_id.value))
