# Define the mapping dictionary
mapping = {
    'B': 'O',
    'b': 'o',
    'Z': 'M',
    'z': 'm'
}

# Open and read the input file
with open("moo_edit.txt", "r") as file:
    text = file.read()

# Perform the mapping
translated_text = "".join(mapping.get(char, char) for char in text)

# Print the result
print(translated_text)
