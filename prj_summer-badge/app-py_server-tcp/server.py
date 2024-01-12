################# IMPORT #################
import server_tools as tools
import socket
import json
from threading import Thread
from base64 import b64encode, b64decode

################# DEF #################
def init_server(backlog:int=5):
    s = socket.socket()
    s.bind(("", tools.PORT))
    print("LOG: server initialization completed")
    while True:
        try:
            s.listen(backlog)
            Thread(target=connect_to_host,args=(s,)).start()
        except socket.error as error:
            print(f"LOG: server initialization failed\n{error}")
            print(f"LOG: server rebooting...")
        
def connect_to_host(s:socket.socket):
    conn, clientAddress = s.accept()
    print(f"LOG: connection established - client: {clientAddress}")
    data = get_data(conn)
    inp_json = convert_in_json(data)
    out_json = process_json(inp_json)
    send_data(conn, out_json)

def get_data(conn:socket.socket) -> bytes:
    conn.settimeout(5.0)
    data = b""
    while True:
        request = conn.recv(4096)
        data += request
        if request[-5:] == b"<end>":
            break
    
    print("LOG: all packages received")
    return data.split(b"<end>")[0]

def convert_in_json(data:bytes) -> dict:
    myjson = json.loads(data.decode())

    if "image" in myjson.keys():
        myjson["image"] = b64decode(myjson["image"])

    return myjson

def process_json(json_data:dict) -> dict:
    print(f"Processing: {json_data}")
    if (json_data["type"] == "get_user_info"):
        return tools.get_user_info(json_data["id"])
    elif (json_data["type"] == "update_entries"):
        return tools.update_entries(json_data["id"],json_data["activities"])
    elif (json_data["type"] == "save_image"):
        return tools.save_image(json_data["id"],json_data["image"])
    elif (json_data["type"] == "save_authorization"):
        return tools.save_authorization(json_data["id"])
    else:
        print("ERROR: invalid function")
    return {}

def send_data(conn:socket.socket, myjson:dict):

    if "image" in myjson.keys():
        myjson["image"] = b64encode(myjson["image"]).decode()

    out_bytes = json.dumps(myjson).encode()
    bytes_string = out_bytes + b"<end>"
    conn.send(bytes_string)

################# CODE #################
if __name__ == "__main__":
    init_server()