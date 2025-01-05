from pwn import *

io = remote('ctf.csd.lol', 5000)

answers = {'1': 'Leviev', '2': 'Microsoft', '3': 'CVE-2024-21302',
 '4': 'EnableVirtualizationBasedSecurity', '5': 'pending.xml', '6': 'ci.dll'}

for i in range(6):
	question = io.recvuntil(f'{list(answers.keys())[i]}: '.encode())
	print(question, end='')
	answer = list(answers.values())[i]
	print(answer)
	io.sendline(answer.encode())
	print(io.recvline())

flag = io.recvall().decode()
print(flag)