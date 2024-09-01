from typing import Union
from common import *


def getPicByMD5(md5 : str, folder : Union[str, None],token: str) -> Union[bool, bytes]:
    if folder is None:
        folder = 'base'
    md5 = md5.lower()
    try:
        with open(upload_url + f"/{token}/" + f"{md5}-{folder}",'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(e)
        return False


def getListPic(folder: Union[str, None], token: str) -> dict:
    pathList = os.listdir(upload_url + f"/{token}/" )
    result_dict = dict()
    for path in pathList:
        md5,raw_folder = path.split("-")
        if folder is None or raw_folder == folder:
            try:
                result_dict[raw_folder].append(md5)
            except:
                result_dict[raw_folder] = [md5]
    return result_dict
