from Crypto.Cipher import AES
import base64

def rotate_matrix(original_matrix):
    """
    Rotates an 8x8 matrix 180 degrees (equivalent to the RM function in the original code)
    """
    length = len(original_matrix)
    rotated = [[0 for _ in range(length)] for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            rotated[j][i] = original_matrix[length - 1 - j][length - 1 - i]
            
    return rotated

def generate_key(matrix):
    """
    Generates the AES key from the white pieces matrix (equivalent to F1 function)
    """
    key = []
    for i in range(8):
        for j in range(8):
            if len(key) < 32:  # We need 32 bytes for AES-256
                # Each byte is piece_value * 16 + row + col
                key.append(matrix[j][i] * 16 + j + i)
    return bytes(key)

def generate_iv(matrix):
    """
    Generates the IV from the rotated black pieces matrix (equivalent to F2 function)
    """
    iv = []
    for i in range(8):
        if len(iv) >= 16:  # We need 16 bytes for the IV
            break
        for j in range(8):
            if len(iv) >= 16:
                break
            # Each byte is piece_value * 2 + (row % 2) + (col % 2)
            iv.append(matrix[j][i] * 2 + j % 2 + i % 2)
    return bytes(iv)

def decrypt_flag(ciphertext, key, iv):
    """
    Decrypts the flag using AES-CBC with PKCS7 padding
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext_bytes = base64.b64decode(ciphertext)
    decrypted = cipher.decrypt(ciphertext_bytes)
    # Remove PKCS7 padding
    padding_length = decrypted[-1]
    return decrypted[:-padding_length].decode('utf-8')

def main():
    # Initialize 8x8 matrices for white and black pieces
    white_matrix = [
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

    black_matrix = [
        [3, 5, 4, 2, 0, 4, 5, 3],
        [6, 6, 6, 6, 6, 6, 6, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Rotate black matrix 180 degrees
    rotated_black = rotate_matrix(black_matrix)
    
    # Generate key and IV
    key = generate_key(white_matrix)
    iv = generate_iv(rotated_black)
    
    # The encrypted flag from the game
    ciphertext = "LlfqPs1MOul1Jr09d6dZditrkXUgIfMDc3Lh6/z5Ufv6E2G8ARHNvE7xQ9jrGBRg"
    
    # Decrypt and print the flag
    try:
        flag = decrypt_flag(ciphertext, key, iv)
        print("Decrypted flag:", flag)
    except Exception as e:
        print("Decryption failed:", str(e))
        print("Key (hex):", key.hex())
        print("IV (hex):", iv.hex())

if __name__ == "__main__":
    main()