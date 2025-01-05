# Hex string from the challenge
hex_data = "25213a2e18213d2628150e0b2c00130e020d024004301e5b00040b0b4a1c430a302304052304094309"

# Convert the hex string to bytes
data = bytes.fromhex(hex_data)

# Password/key to XOR
key = b"long_strange_trip"

# Repeat the key to match the length of the data
repeated_key = (key * (len(data) // len(key) + 1))[:len(data)]

# XOR the data with the repeated key
decrypted = bytes([d ^ k for d, k in zip(data, repeated_key)])

# Print the result as a string
print("Decrypted text:", decrypted.decode(errors="replace"))
