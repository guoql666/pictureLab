from aiohttp import web
from download import *
from upFile import *
from common import *

route = web.RouteTableDef()


# 上传图片
@route.post("/PicUpload")
async def PicUpload(request):
    get_data = dict(request.query)
    # 校验是否存在token且是否合法
    if check_token(get_data.get('token')) is False:
        error_result = {'error':'token expired'}
        return web.json_response(error_result,status=403)
    try:
        post_data = await request.multipart()
    except AssertionError as e:
        error_result = {'error':str(e)}
        return web.json_response(error_result,status=404)
    # 分段获取post数据
    field = await post_data.next()
    
    try:
        # 找到payload数据
        while field.name != 'payload':
            field = await post_data.next()
    except:
        # 如果报错(yeild Error)则说明不存在相关字段，返回
        error_result = {'error':'file data not found'}
        return web.json_response(error_result,status=404)
    
    folder = get_data.get('path')
    # 如果result为真，那么会返回filename,否则返回None
    result,filename = await UploadFile(field,folder)
    if result:
        web.json_response({'message':'upload success','info':{'md5':str(filename)}},status=200)
    else:
        error_result = {'error':'file upload faild'}
        return web.json_response(error_result,status=404)


# 下载图片
@route.get("/PicDownload")
async def Picture(request):
    data = dict(request.query)
    # 校验是否存在token且是否合法
    if check_token(data.get('token')) is False:
        error_result = {'error':'token expired'}
        return web.json_response(error_result,status=403)
    md5 = data.get('file')
    folder = data.get('path')
    # 校验md5是否合法，避免存在路径穿越
    if not check_md5(md5):
        error_result = {'error':'filename valid'}
        return web.json_response(error_result,status=404)
    # 获取图片
    pic_file = getPicByMD5(md5,folder)
    # 图片无法读取或不存在
    if pic_file is False:
        error_result = {'error':'file not exist'}
        return web.json_response(error_result,status=404)
    return web.Response(body=pic_file)


# 从url下载图片
@route.get("/PicUploadFromUrl")
async def PicUploadUrl(request):
    data = dict(request.query)
    if check_token(data.get('token')) is False:
        error_result = {'error':'token expired'}
        return web.json_response(error_result,status=403)
    
    if url:=data.get('url') is None:
        error_result = {'error':'url required'}
        return web.json_response(error_result,status=404)
    folder = data.get('path')
    # 如果result为真，那么会返回filename,否则返回None
    result,filename = await UploadFileFromUrl(url,folder)
    if result:
        web.json_response({'message':'upload success','info':{'md5':str(filename)}},status=200)
    else:
        error_result = {'error':'file upload faild'}
        return web.json_response(error_result,status=404)


def main():
    app = web.Application()
    app.add_routes(route)
    web.run_app(app, host="127.0.0.1", port=5000)


if __name__ == "__main__":
    main()