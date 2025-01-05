import tiktoken

# Token IDs from the challenge
token_ids = [
    17360, 3575, 553, 261, 10297, 29186, 1428, 8256, 5485, 668, 290, 9641, 13,
    62915, 0, 7306, 382, 290, 9641, 25, 220, 15, 4645, 90, 67, 15, 22477, 15,
    84, 62, 7316, 91, 15, 37313, 62, 10, 72, 42, 10, 525, 18, 77, 16, 57, 18,
    81, 30, 92, 1428, 13659, 481, 0, 15334, 261, 1899, 1058, 540, 220, 15, 308, 69, 1323, 19, 0
]

# Initialize the tokenizer for the `gpt-4o` model
# encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model('gpt-4o')


# Decode the token IDs into text
decoded_text = encoding.decode(token_ids)

print("Decoded Text:")
print(decoded_text)
