# XOR each byte of the obfuscated_key with 0x7f
obfuscated_key = [0xf, 0xd, 0x16, 0x11, 0x18, 0x13, 0x1a, 0xc, 0x4f, 0x46, 0x5c]

passcode = ''.join(chr(byte ^ 0x7f) for byte in obfuscated_key)

print("Recovered Passcode:", passcode)