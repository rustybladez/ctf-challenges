# Hex values from the binary
local_68 = 0x633563607c514e54
local_60 = 0x7e60773453607a

# Combine them into a single byte array
combined_bytes = local_68.to_bytes(8, 'little') + local_60.to_bytes(7, 'little')

# Compute the flag by incrementing each byte
flag = ''.join(chr(b - 1) for b in combined_bytes)
print("Flag:", flag)
