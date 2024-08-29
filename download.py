from typing import Union
from common import *


def getPicByMD5(md5 : str, folder : Union[str, None]) -> Union[bool, bytes]:
    if folder is None:
        folder = 'base'
    md5 = md5.lower()
    try:
        with open(upload_url + f"{md5}-{folder}",'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError as e:
        print(e)
        return False
    
