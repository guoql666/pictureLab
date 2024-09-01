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
    

def md5_calc(md5_hash, data: bytes):
    md5_hash.update(data)
    return md5_hash


def folder_init():
    for token in token_list:
        if not os.path.isdir(upload_url + f"/{token}/"):
            os.mkdir(upload_url + f"/{token}/")


def IsPicExist(target_md5: str, folder: str, token: str) -> bool:
    if folder is None:
        folder = "base"
    pathList = os.listdir(upload_url + f"/{token}/" )
    for path in pathList:
        md5,raw_folder = path.split("-")
        if folder == raw_folder and md5 == target_md5:
            return True
    return False
