def gbk_demo():
    data = "百度一下".encode("GBK")  #使用gbk编码
    u_data = "百度一下".encode("utf-8")  #使用utf-8编码
    print("gkb编码：",data)
    print("utf-8编码：",u_data)
    res_data = data.decode("GBK")
    res_udata = u_data.decode("utf-8")
    print("使用GBK解码：", res_data)
    print("使用utf-8解码：", res_udata)
gbk_demo()


import chardet

message = "哈哈".encode()
print("查询默认编码方式：",chardet.detect(message))

