import struct

packed = struct.pack("<I f 5s", 42, 3.14, b"hello")
print(packed, len(packed))               # 13 bytes
print(struct.unpack("<I f 5s", packed))