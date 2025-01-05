import zlib

# Read the compressed data
with open("5B.zlib", "rb") as f:
    compressed_data = f.read()

# Initialize decompression object with wbits=-15
decompressor = zlib.decompressobj(wbits=-15)

try:
    decompressed_data = decompressor.decompress(compressed_data)
    decompressed_data += decompressor.flush()
    print("Decompressed data:", decompressed_data.decode())
except zlib.error as e:
    print("Decompression error:", e)
