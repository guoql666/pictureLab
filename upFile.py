from typing import Union,Tuple
from common import *
import hashlib
from time import time
import aiohttp

async def UploadFile(payload,folder : Union[str, None]) -> bool:
    if folder is None:
        folder = "base"
    # 防止异步造成文件名资源互斥，用时间来区分
    temp_filename = str(time())
    # 计算md5
    md5_hash = hashlib.md5()
    # 计算size
    size = 0
    with open(upload_url + f"{temp_filename}-{folder}","wb") as file:
        while True:
            chunk = await payload.read_chunk()
            if not chunk:
                break
            # 更新md5
            md5_hash = md5_calc(md5_hash, chunk)
            # 写入文件
            file.write(chunk)
            # 更新size大小
            size += len(chunk)
    # 计算md5文件名
    filename = md5_hash.hexdigest()
    # 重命名
    os.rename(upload_url + f"{temp_filename}-{folder}", upload_url + f"{filename}-{folder}")
    #若size为0，说明文件未正常传输或为空文件
    if size == 0:
        os.remove(upload_url + f"{filename}-{folder}")
        return False,None
    return True,filename


async def UploadFileFromUrl(url: str, folder: Union[str, None]) -> Tuple[bool, Union[None, str]]:
    if folder is None:
        folder = "base"
    async with aiohttp.request("GET",url) as res:
        resp_code = res.status
        data = await res.read()
    # 下载是否成功
    if resp_code != 200:
        return False,None
    if len(data) == 0:
        return False,None
    filename = hashlib.md5(data).hexdigest()
    with open(upload_url + f"{filename}-{folder}","wb") as file:
        file.write(data)
    return True,filename
