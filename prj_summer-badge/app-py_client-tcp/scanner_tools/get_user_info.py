################# IMPORT #################
import scanner_tools as tools

################# DEF #################
def get_user_info(id:str) -> dict:
    myjson = {"type":"get_user_info","id":id}
    out = tools.send_json(myjson)
    return out

################# CODE #################
if __name__ ==  "__main__":
    pass