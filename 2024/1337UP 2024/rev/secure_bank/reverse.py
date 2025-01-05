def obscure_key(param_1):
    # XOR with 0xa5a5a5a5
    # temp = param_1 ^ 0xa5a5a5a5
    # # Circular left shift by 3 and right shift by 29
    # temp = ((temp << 3) | (temp >> 29)) & 0xFFFFFFFF  # Ensure 32-bit limit
    # # Multiply by 0x1337 and XOR with 0x5a5a5a5a
    # temp = (temp * 0x1337) & 0xFFFFFFFF  # Ensure 32-bit limit
    # return temp ^ 0x5a5a5a5a

    temp = ((param_1 ^ 0xa5a5a5a5) << 3 | (param_1 ^ 0xa5a5a5a5) >> 0x1d) * 0x1337 ^ 0x5a5a5a5a
    return temp

def generate_2fa_code(param_1):
    local_10 = param_1 * 0xBEEF
    local_c = local_10
    for local_14 in range(10):
        local_c = obscure_key(local_c)
        # Rotate and combine results
        local_10 = ((local_10 ^ local_c) << 5 | (local_10 ^ local_c) >> 0x1b) + (local_c << (chr(local_14) + chr((local_14 // 7)) * -7 & 0x1f) ^ local_c >> (chr(local_14) + chr((local_14 // 5)) * -5 & chr(0x1f)))  # Ensure 32-bit limit
    return local_10 & 0xFFFFFF  # Return least significant 24 bits

# PIN is 1337 (0x539)
pin = 1337
two_fa_code = generate_2fa_code(pin)
print(f"Generated 2FA Code: {two_fa_code}")
