################# IMPORT #################
import scanner_tools as tools
import socket, sys, json
from base64 import b64encode, b64decode

################# DEF #################
def send_json(myjson:dict) -> dict:

    if "image" in myjson.keys():
        myjson["image"] = b64encode(myjson["image"]).decode()

    str_dict = json.dumps(myjson)
    s = connect_to_server()
    s.send(str_dict.encode() + b"<end>")
    bytes_out = get_trasmission(s)
    s.close()
    dict_out = process_data(bytes_out)
    return dict_out

def connect_to_server() -> socket.socket:
    try:
        s = socket.socket()
        s.connect((tools.IP, tools.PORT))
        print(f"LOG: server connection established")
    except socket.error as error:
        print(f"LOG: server connection failed\n{error}")
        sys.exit()
    return s

def get_trasmission(s:socket.socket) -> bytes:
    s.settimeout(5.0)
    data = b""
    while True:
        request = s.recv(4096)
        data += request
        if request[-5:] == b"<end>":
            break
    return data.split(b"<end>")[0]

def process_data(data:bytes) -> dict:
    myjson = json.loads(data.decode())

    if "image" in myjson.keys():
        myjson["image"] = b64decode(myjson["image"])

    print("LOG: message recived")
    return myjson

################# CODE #################
if __name__ ==  "__main__":
    pass