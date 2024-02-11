#!/usr/bin/env python3

import telnetlib, json
import base64, codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes


HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

####### DEF #######
def msg_decode(type:str, encoded) -> bytes:
    print(type, encoded)
    if type == 'bigint':
        return long_to_bytes(int(encoded[2:], 16))
    elif type == 'utf-8':
        return ''.join([chr(i) for i in encoded]).encode()
    elif type == 'base64':
        return base64.b64decode(encoded)
    elif type == 'hex':
        return bytes.fromhex(encoded)
    elif type == 'rot13':
        return codecs.decode(encoded, 'rot_13').encode()

####### CODE #######
for i in range(100):    
    req = tn.read_until(b"\n").decode()[:-1]
    dict_req = json.loads(req)
    r = msg_decode(**dict_req).decode()
    r_dict = {'decoded': r}
    r_bytes_dict = json.dumps(r_dict).encode()
    tn.write(r_bytes_dict)

tn.interact()