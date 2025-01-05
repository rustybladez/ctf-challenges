# Decimal values from the binary
headKey = [65, 85, 44, -125]  # Convert to unsigned
meowMeow = [
    25, 32, -123, 2, 55, 60, 41, 2, 45, 72, 48, -59,
    73, 30, 115, -58, 78, 34, 96, -48, 87
]  # Convert to unsigned

# Convert signed values to unsigned (0-255 range)
headKey = [k & 0xFF for k in headKey]
meowMeow = [m & 0xFF for m in meowMeow]

# Compute the flag
flag = []
for i in range(21):  # Flag is 21 characters long
    char = ((meowMeow[i] - i - 7) ^ headKey[i % 4]) & 0xFF
    flag.append(chr(char))

# Join and display the flag
flag = ''.join(flag)
print(f"Flag: {flag}")
