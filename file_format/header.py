import struct


# char magic[64]
# uint32_t format_version
# uint16_t protocol_major
# uint16_t protocol_minor
# int64_t timestamp
# char name[32]
# char credits[32]
header_format = "<64sIHHq32s32s"


def create_header(format_version: int, protocol_version: tuple[int, int], timestamp: int, name: str, creator: str):
    magic = b"AERIAL FILE FORMAT https://github.com/NiyazBiyaz/aerial".ljust(64, b"\x00")
    name = name.encode().ljust(32, b"\x00")
    creator = creator.encode().ljust(32, b"\x00")

    major, minor = protocol_version

    return struct.pack(header_format, magic, format_version, major, minor, timestamp, name, creator)


if __name__ == "__main__":
    import time
    with open("empty.aerial", "wb") as f:
        f.write(create_header(1, (1, 1), round(time.time()), "Empty Aerial File", "NiyazBiyaz"))
