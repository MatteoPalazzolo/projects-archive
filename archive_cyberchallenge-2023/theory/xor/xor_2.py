from Crypto.Util.number import bytes_to_long, long_to_bytes

KEY1 = bytes_to_long(bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'))
KEY23 = bytes_to_long(bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'))
KEY4 = bytes_to_long(bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'))

flag = KEY1 ^ KEY23 ^ KEY4

flag = long_to_bytes(flag).decode()
print(flag)