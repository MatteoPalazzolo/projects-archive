### FLAG 1
# m1 = bytes.fromhex('158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf')
# m2 = bytes.fromhex('73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2')
# 
# def xor(a: bytes, b: bytes) -> bytes:
#   return bytes([x^y for x,y in zip(a,b)])
# 
# out = xor(m1, m2)
# print(out)


### FLAG 2
# ciphertext = bytes.fromhex('104e137f425954137f74107f525511457f5468134d7f146c4c')
# 
# for i in range(1, 256):
#   out = bytes([i^c for c in ciphertext])
#   print(out)
