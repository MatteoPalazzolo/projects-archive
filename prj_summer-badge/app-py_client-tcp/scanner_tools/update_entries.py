################# IMPORT #################
import scanner_tools as tools

################# DEF #################
def update_entries(id:str,activities:list) -> dict:
    myjson = {"type":"update_entries","id":id,"activities":activities}
    out = tools.send_json(myjson)
    return out

################# CODE #################
if __name__ ==  "__main__":
    pass