from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def _DES_():
  key = bytes.fromhex('04a7a2ed1667b678')
  cipher = DES.new(key, DES.MODE_CBC)
  plaintext = 'La lunghezza di questa frase non è divisibile per 8'
  msg = cipher.encrypt(pad(plaintext.encode(), 8, style='x923')).hex()

  print(msg)
  print(cipher.iv.hex())



from Crypto.Cipher import AES

def _AES256_():
  key = bytes.fromhex('395ff673395ff673395ff6730011550000')
  cipher = AES.new(key, AES.MODE_CFB)
  cipher.segment_size = 24 
  plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
  msg = cipher.decrypt(pad(plaintext.encode(), 16, style='pkcs7'))
  
  print(msg)


ALGORITMI = [_DES_, _AES256_]

ALGORITMI[int(input('Quale? '))]()