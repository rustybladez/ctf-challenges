import string

# Generate all combinations
vowels = ['a', 'e', 'i', 'o', 'u']
guess = ['F', 'V', 'J']
# combinations = [f"d{char1}{char2}0" for char1 in vowels for char in string.ascii_uppercase]
combinations = [f"d{char1}{char2}0" for char1 in vowels for char2 in guess]

# Print or save the results
for combo in combinations:
    print(combo)
