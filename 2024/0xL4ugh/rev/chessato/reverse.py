import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import numpy as np

def rm(original_matrix):
    """Rotate the matrix 180 degrees."""
    original_matrix = np.array(original_matrix)  # Convert to NumPy array
    length = len(original_matrix)
    array = np.zeros((length, length), dtype=int)
    for i in range(length):
        for j in range(length):
            array[j, i] = original_matrix[length - 1 - j, length - 1 - i]
    return array

def f1(matrix):
    """Calculate the AES key (32 bytes) from the 8x8 matrix."""
    array = bytearray(32)
    num = 0
    for i in range(8):
        for j in range(8):
            if num < len(array):
                array[num] = matrix[j][i] * 16 + j + i
                num += 1
    return bytes(array)

def f2(matrix):
    """Calculate the AES IV (16 bytes) from the 8x8 matrix."""
    array = bytearray(16)
    num = 0
    for i in range(8):
        if num >= len(array):
            break
        for j in range(8):
            if num >= len(array):
                break
            array[num] = matrix[j][i] * 2 + j % 2 + i % 2
            num += 1
    return bytes(array)

def aes_decrypt(ciphertext, key, iv):
    """Decrypt the ciphertext using AES (CBC mode) with the given key and IV."""
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted = aes.decrypt(base64.b64decode(ciphertext))
    try:
        plaintext = unpad(decrypted, AES.block_size)
        return plaintext.decode('utf-8')
    except (ValueError, UnicodeDecodeError) as e:
        print(f"Error during decryption: {e}")
        return decrypted  # Return raw bytes for debugging

# Input matrices (example for testing; replace with actual matrices from the game logic)
array_white = [
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [0, 0, 0, 0, 0, 0, 0, 0],  
    [6, 6, 6, 6, 6, 6, 6, 6], 
    [3, 5, 4, 2, 0, 4, 5, 3],  
]

# King: 1 Queen: 2 Rook: 3 Bishop: 4 Knight: 5 Pawn: 6

array_black = [
    [3, 5, 4, 2, 0, 4, 5, 3],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Hardcoded ciphertext from the game
ciphertext = "LlfqPs1MOul1Jr09d6dZditrkXUgIfMDc3Lh6/z5Ufv6E2G8ARHNvE7xQ9jrGBRg"

# Calculate the rotated matrix
rotated_matrix = rm(array_black)

# Generate the AES key and IV
key = f1(array_white)
iv = f2(rotated_matrix)

# Debug key and IV
print(f"Key (hex): {key.hex()}")
print(f"IV (hex): {iv.hex()}")

# Decrypt the ciphertext
flag = aes_decrypt(ciphertext, key, iv)

# Output the flag
print(f"Decrypted Flag: {flag}")
