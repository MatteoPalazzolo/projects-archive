from Crypto.Util.number import bytes_to_long, long_to_bytes
import pwn

word = "label"
num = 13

print(pwn.xor(word, num))

for i in word:
    xor = ord(i) ^ 13
    print(chr(xor), end='')