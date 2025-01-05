import hashlib
import string

# Load hashes from the file
with open('pieces.txt', 'r') as f:
    hashes = [line.strip() for line in f]

# Starting flag from known decrypted values
current_flag = ""

# Printable characters to test (letters, numbers, and symbols)
characters = string.printable.strip()  # Removes the newline character from the printable set

# Iterate through the hashes
for i, target_hash in enumerate(hashes[len(current_flag):], start=len(current_flag) + 1):
    found = False
    for char in characters:
        # Add the character to the current flag and hash it
        candidate = current_flag + char
        candidate_hash = hashlib.sha256(candidate.encode()).hexdigest()
        
        # Compare with the target hash
        if candidate_hash == target_hash:
            current_flag += char
            print(f"Found character {i}: {char}")
            found = True
            break
    
    if not found:
        print(f"Could not find a matching character for line {i}")
        break

# Print the full flag
print(f"Full flag: {current_flag}")
