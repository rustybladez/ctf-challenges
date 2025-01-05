# Read the input file
with open("BeeInSpace.txt", "r") as f:
    data = f.read()

# Map spaces to '0' and tabs to '1'

binary_data = ""

# Identify tab width and map to binary
for char in data:
    # Check if the character is a tab
    if char == "\t":
        # Determine the width of the tab
        if data[data.index(char):data.index(char)+2] == "\t\t":
            binary_data += "0"  # 2-space tab as '0'
        else:
            binary_data += "1"  # 4-space tab as '1'
print(binary_data)
# Split binary data into 8-bit chunks
ascii_text = ""
for i in range(0, len(binary_data), 8):
    byte = binary_data[i:i+8]
    if len(byte) == 8:  # Ensure full 8-bit bytes
        # Convert to ASCII
        ascii_text += chr(int(byte, 2))

# Print the decoded message
print("Hidden message:", ascii_text)
