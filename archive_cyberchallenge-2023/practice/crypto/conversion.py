### FLAG 1
# l = [102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]
# for i in l:
#   print(chr(i), end="")
# print()

print()
print('INT - CHAR')
print(chr(5), ord('a'))
print()


### FLAG 2
# b = bytes.fromhex('666c61677b68337834646563696d616c5f63346e5f62335f41424144424142457d').decode()
# print(b)

print('STRING - HEX')
print('bztesz'.encode().hex(), bytes.fromhex('666c6167').decode())
print()


### FLAG 3
from base64 import b64decode, b64encode
# 
# print(b64decode(b'ZmxhZ3t3NDF0XzF0c19hbGxfYjE=').decode(), end="")
# n = 664813035583918006462745898431981286737635929725
# print(n.to_bytes(n.bit_length(),'big').decode())

print('B64 - BYTES')
print(b64decode(b'ZmxhZ3t3NDF0XzF0c19hbGxfYjE=').decode())
print(b64encode(b'flag{w41t_1ts_all_b1').decode())
print()

print('INT - BYTES')
print((50).to_bytes((50).bit_length(), 'big'))
print(int.from_bytes(b'/x00/x005/00', 'big'))
print()