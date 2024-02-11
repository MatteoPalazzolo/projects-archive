from Crypto.Util.number import bytes_to_long, long_to_bytes

_int = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
r = long_to_bytes(_int).decode()

print(r)