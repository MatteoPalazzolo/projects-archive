import pwn

KEY1 = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(256):
    res = pwn.xor(KEY1, i)
    print(res)