import pwn

conn = pwn.remote('130.192.5.212', 17384)



# 1) SUM
print(conn.recvuntil(b'func(int64_t n1, int64_t n2, int64_t n3)').decode())

with open('sum.s','r') as file:
  s = pwn.asm(file.read(), arch="amd64")
conn.sendline(s)

print(conn.recvline().decode())
print(conn.recvline().decode())
print(conn.recvline().decode())



# 2) COMPARE
print(conn.recvuntil(b'func(int64_t n1, int64_t n2, int64_t n3)').decode())

with open('compare.s','r') as file:
  s = pwn.asm(file.read(), arch="amd64")
conn.sendline(s)

print(conn.recvline().decode())
print(conn.recvline().decode())
print(conn.recvline().decode())



# 3) MULT
print(conn.recvuntil(b'func(int64_t n1)').decode())

with open('mult.s','r') as file:
  s = pwn.asm(file.read(), arch="amd64")
conn.sendline(s)


conn.interactive()

print(conn.recvlines(3).decode())
print(conn.recvline().decode())
print(conn.recvline().decode())
