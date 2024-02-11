from Crypto.PublicKey import RSA

with open('./data_formats/privacy_enhanced_mail.pem','r') as pem:
    key = RSA.importKey(pem.read())

'''
print(key.n)
print(key.d) // private key : int
print(key.e)
print(key.p)
print(key.q)
print(key.u)
'''

print(key.d)