import pwn

KEY1 = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
KEY2 = 'crypto{'.encode()

for n in range(256):
    key = pwn.xor(KEY1[:len(KEY2)] + chr(n).encode(), KEY2)
    res = pwn.xor(KEY1, key)
    try:
        res = res.decode()
        if res.endswith('}') and res[7:9] == 'if':
            print(res)
    except UnicodeDecodeError:
        pass

