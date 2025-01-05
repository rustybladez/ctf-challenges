from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from binascii import unhexlify

# Given data
key = b"1234567890abcdef1234567890abcdef"  # Convert the key to bytes
enc_flag = (
    "f1cbfba19daa8a12ed682293dd82ec0c53e0c48a2501a1ea689feb9d8787de3c"
    "ef2b7de5a08d50ecc320f5f252b4dc4519605c3a9e8cd4e3b9b95ee11164186d"
    "fa77a6c67e940d35e7d4d3c092745d773a1d61c4778d2ad64c6ac85d40f0b5ba"
    "a967c32f21f85617d2a8cdeb57fe238fc25723207ec4e517797052e7eaa6aebf"
    "48f4cb3d731782e3"
)

# Decode the ciphertext from hex to bytes
ciphertext = unhexlify(enc_flag)

# Ensure ciphertext is aligned to block boundary (16 bytes)
# If not aligned, pad it with zeros (or any appropriate padding)
if len(ciphertext) % 16 != 0:
    ciphertext = pad(ciphertext, 16)

# Initialize AES cipher in ECB mode
cipher = AES.new(key, AES.MODE_ECB)

# Decrypt the ciphertext
plaintext = cipher.decrypt(ciphertext)

# Try to decode as UTF-8, ignoring invalid characters
print(plaintext.decode('utf-8', errors='ignore'))
