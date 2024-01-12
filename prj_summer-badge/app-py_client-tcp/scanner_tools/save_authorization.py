################# IMPORT #################
import scanner_tools as tools

################# DEF #################
def save_authorization(id:str) -> dict:
    myjson = {"type":"save_authorization","id":id}
    out = tools.send_json(myjson)
    return out

################# CODE #################
if __name__ ==  "__main__":
    pass