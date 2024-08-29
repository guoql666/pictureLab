from config import *


def check_token(token : str) -> bool:
    return token in token_list


def check_md5(md5:str) -> bool:
    try:
        # md5一定为16进制字符串
        int(md5,16)
        return True
    except:
        return False
    

def md5_calc(md5_hash,data):
    md5_hash.update(data)
    return md5_hash