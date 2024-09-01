## usage

​	提供上传和下载服务

​	提供path参数用来标注文件分类，默认为base，通过get方式传输

​	请您务必不要泄露token，程序并未对token持有者设置过多安全防护

### 下载

​	下载uri为/PicDownload

​	需要欲下载文件的md5值，可选参数path

​	/PicDownload?token=xxx&file=yyy

​	

### 上传

​	上传有两种方式，一种为直接上传

​	另一种为通过url从远程服务器下载到图库

​	直接上传需要通过form表单的形式传输

​	您需要通过get提供token参数
​	folder参数可选

​	/PicUpload?token=xxx

​	并通过post方式传递form表单。

​	图库会读取payload字段的内容并写入文件



​	通过url上传则需要提供对应的url

​	自然地，您也需要提供token才可进行上传

​	通过get方式传输欲下载的URL

​	/PicUploadFromUrl?token=xxx&url=yyy


## 查询
    目前提供了两种查询图片是否存在的方式，您可以根据需求来进行查看

    1.

    通过/PicList?token=xxx来获取所有图片列表

    指定path来获取不同分类的图片列表，此处缺省则返回所有分类图片

    2.
    
    通过/PicExist?token=xxx&md5=yyy来获取指定md5的图片信息

    path参数可选输入，来获取不同分类的目录

    (3).

    此外，您仍可以通过尝试下载的方式来检测该文件是否存在，但我们不建议您使用该方式，因为该下载方式后续可能发生更改而导致您的代码出现问题

    请在可以的情况下，使用上述两种方式进行搜索和查看

    


## TODO

- [ ] 上传
    - [ ] 限制后缀
    - [x] 文件夹分类
    - [x] 从url上传

- [x] 下载
    - [x] 通过图片MD5下载
  
- [x] 安全
    - [x] 路径穿越
    - [x] 任意文件读取

- [x] 权限
    - [x] token验权

- [x] 运维
    - [x] log输出
    - [x] 异步处理 
