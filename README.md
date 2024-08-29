## usage

​	提供上传和下载服务

​	提供folder参数用来标注文件分类，默认为base，通过get方式传输

​	请您务必不要泄露token，程序并未对token持有者设置过多安全防护

### 下载

​	下载uri为/PicDownload

​	需要欲下载文件的md5值，可选参数folder

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
