import base64

_hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
_bytes = bytes.fromhex(_hex)
r = base64.b64encode(_bytes)

print(r.decode())