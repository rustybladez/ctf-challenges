def decode_binary(binary_list, multiplier):
    decoded = []
    for binary in binary_list:
        # Convert binary to integer
        num = int(binary, 2)
        # Reverse the multiplication to get the ASCII value
        ascii_val = num // multiplier
        # Convert ASCII value to character
        decoded.append(chr(ascii_val))
    return ''.join(decoded)

# Constants
z = 69
w = 67
multiplier = z + w  # 136

# Binary strings from binary.txt
binary_data = """
10110000011000 10100011101000 10101010000000 100000101011000 10010100110000
1101000001000 11001110001000 11011010111000 11001001111000 10010100110000
10100111111000 10101110010000 11001001111000 1001010011000 10100001100000
1100110000000 11111010110000 11010110101000 100001001101000
"""

# Decode the binary strings
binary_list = binary_data.strip().split()
decoded_message = decode_binary(binary_list, multiplier)
print("Decoded Message:", decoded_message)
