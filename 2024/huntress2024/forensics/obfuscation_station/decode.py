import base64
import zlib

data = base64.b64decode('UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA')
decompressed_data = zlib.decompress(data, -zlib.MAX_WBITS)
print(decompressed_data.decode('ascii'))
