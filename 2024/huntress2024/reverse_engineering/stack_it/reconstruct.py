from pwn import *

# Open the binary in pwntools to read bytes
bin_file = ELF('stack_it.bin')

# Addresses for the XOR data arrays
data1_addr = 0x0804a00e  # Address of &DAT_0804a00e
data2_addr = 0x0804a02e  # Address of &DAT_0804a02e
flag_start = "flag{"
flag_end = "}"

# Read the 32 bytes from each data address
data1 = bin_file.read(data1_addr, 32)
data2 = bin_file.read(data2_addr, 32)

print("Data at data1_addr:", data1)
print("Data at data2_addr:", data2)

# XOR corresponding bytes from data1 and data2
flag_middle = ''.join(chr(b1 ^ b2) for b1, b2 in zip(data1, data2))

# Construct the full flag
flag = flag_start + flag_middle + flag_end
print("Flag:", flag)
