from pwn import xor

# Ciphertexts from dist.txt
ciphertexts = [
    bytes.fromhex(ct) for ct in [
        '43794c9c8faa2cff24edc8afe507a13f62837c7e166f428cab5aff893225ff19104bc8754c1c09', 
          '5d315e8786e62cf763e9d4afe80ca13b649a717e11615986b642f3952f76b71b0342c4', 
          '46785a8bcae62aeb60a5deeef107a1256ed7792752695886ff50f5886171ff1717', 
          '5d315e819fe621b966e08dfae906e43a78837b31162e5e8cff46e8953275f20a0d5ad23d4712144c', 
          '557f4dce9ee220b967e4dfffe616e9216a9934291b7d5690bb45ba922e6afc', 
          '55315a868fef35f16beac6afe810a1206a81717e1e6b5690b152ba953462ff0c424acd6e0307055a81b93590c1fe', 
          '557d489dcafd2df870a5cfe0e816f268628334291b7a5fc2aa58f99f3276f616160fc27c5116', 
          '557f4dce8bee21fc24f1c5eaa712ee3f6e853431142e448db216fb9e2b70e5110c48816b46011e5a', 
          '407e099783ef29fd24edc4fca704f33d6283343f1c6a178ab645ba962464f1581147c0714f530350d5f53690dee6', 
          '40785ace93e530b970edccfba711e0312b9e607e1c6143c2b616e3953425f317425bc9780317085ac5a6', 
          '41754a9a8cf13da976dac4e1d810b1253f994b6f47514387b106e8a57175a40a0370d22c4d14084d9ea8'
    ]
]

# Known part of the flag
known_plaintext = b'udctf{'

# Attempt to find the ciphertext that corresponds to the flag
for ct in ciphertexts:
    if len(ct) >= len(known_plaintext):
        # Extract the portion of the ciphertext corresponding to the known plaintext
        ct_segment = ct[:len(known_plaintext)]
        
        # XOR to find the partial key
        partial_key = xor(ct_segment, known_plaintext)
        print(f'Partial key from ciphertext: {partial_key}')
        
        # Try decrypting the entire ciphertext with this partial key repeated
        possible_plaintext = xor(ct, partial_key * (len(ct) // len(partial_key) + 1))[:len(ct)]
        
        # Check if the decrypted text contains readable words or the flag format
        if b'udctf{' in possible_plaintext:
            print(f'Decrypted plaintext (possible flag): {possible_plaintext}')
