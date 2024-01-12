################# IMPORT #################
import scanner_tools as tools

################# DEF #################
def save_image(id:str,image:bytes) -> dict:
    myjson = {"type":"save_image","id":id,"image":image}
    out = tools.send_json(myjson)
    return out

################# CODE #################
if __name__ ==  "__main__":
    pass