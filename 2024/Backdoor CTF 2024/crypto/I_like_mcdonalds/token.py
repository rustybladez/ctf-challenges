import hashlib
import random
import string
from collections import defaultdict

class CustomMAC:
    def __init__(self, key: bytes):
        self._internal_state = b""
        self._key = key
        
    def update(self, message: bytes) -> None:
        if not self._internal_state:
            self._internal_state = self._key + message
        else:
            self._internal_state += message
            
    def digest(self) -> bytes:
        return hashlib.sha256(self._internal_state).digest()[:8]

# Simulate the MAC service to find collisions
def find_collisions(key: bytes, target_collisions: int = 64):
    mac = CustomMAC(key)
    mac_collisions = defaultdict(list)
    
    while len(mac_collisions) < target_collisions:
        # Generate random messages
        message = ''.join(random.choices(string.ascii_letters + string.digits, k=16)).encode()
        
        # Compute MAC
        mac.update(message)
        digest = mac.digest()
        
        # Store collisions
        mac_collisions[digest].append(message)
        
        if len(mac_collisions[digest]) >= target_collisions:
            break
            
    return mac_collisions

# Generate the message-token pairs
def generate_pairs(key: bytes, num_pairs: int = 64):
    collisions = find_collisions(key, target_collisions=num_pairs)
    pairs = []
    
    for digest, messages in collisions.items():
        for msg in messages:
            pairs.append((msg, digest))
            if len(pairs) >= num_pairs:
                break
        if len(pairs) >= num_pairs:
            break
    
    return pairs

# Example usage
if __name__ == "__main__":
    # Replace with the actual key or simulate one
    simulated_key = b"example_secret_key"
    
    # Generate 64 message-token pairs
    message_token_pairs = generate_pairs(simulated_key, 64)
    
    for msg, token in message_token_pairs:
        print(f"Message: {msg.hex()}, Token: {token.hex()}")
