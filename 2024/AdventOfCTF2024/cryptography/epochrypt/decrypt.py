import time
import base64 as b64
from pwn import xor

# Given encrypted flag (hex string)
encrypted_flag_hex = "6b59695b575e5406676d7f5e6671555d79597d0e57707a0664647e06560b5c7677640c0e"

# Step 1: Convert hex string to bytes
encrypted_flag = bytes.fromhex(encrypted_flag_hex)

# Step 2: Brute-force the epoch time
current_epoch = int(time.time())  # Current epoch time
start_epoch = current_epoch - 60  # Assume encryption happened within the last 60 seconds
end_epoch = current_epoch + 60    # Account for slight time drift

for epoch_guess in range(start_epoch, end_epoch):
    # Convert epoch guess to bytes
    epoch_bytes = str(epoch_guess).encode()

    # Step 3: XOR the encrypted flag with the epoch bytes
    base64_encoded = xor(encrypted_flag, epoch_bytes)

    try:
        # Step 4: Decode the Base64-encoded data
        byte_manipulated = b64.b64decode(base64_encoded)

        # Step 5: Reverse the byte manipulation
        original_flag = bytes([(b - 3) % 256 for b in byte_manipulated])

        # Print the results
        # print(f"Epoch Guess: {epoch_guess}")
        print(f"Decoded Flag: {original_flag.decode()}")
    except Exception:
        # If decoding fails, continue to the next guess
        continue
