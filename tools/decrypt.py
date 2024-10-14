# -*- encoding: utf-8 -*-
'''
@时间 ： 2024/7/16 10:52
@作者 ： WangQitao
@名称 ： decrypt.py 
@描述 ：
'''
import inspect
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from Crypto.Cipher import AES
import urllib.parse
import base64


def decrypt_url(url):
    """解密营销链接"""
    try:
        # base64解密
        base_data = base64.b64decode(url).decode('utf-8')
        # AES128解密
        key = "uJhXC7qm6qoju1kF"
        key = key.encode()  # 将密钥转换为字节型
        cipher = AES.new(key, AES.MODE_ECB)  # 创建AES对象，使用ECB模式
        aes_data = cipher.decrypt(base64.b64decode(base_data)).decode('utf-8')
        # URL解密
        url_data = urllib.parse.unquote(urllib.parse.unquote(aes_data))
        return url_data
    except Exception as e:
        print(f"函数 {inspect.stack()[0][3]} : 报错异常 - {e}")


if __name__ == '__main__':
    url = "https://www.diskpart.com/cart?eurl=aWZlSFdkaXloQ0o0N25JczdyQ1dObDRLMmtXck9mdXZnV1ZXVGVQSzhxY3dkdHZ6SVgvTHZEcUVEU2c3QmlmUHRCQ2lQZnVSTjJGV1BxcjJSUVBvNHJNRzFLa2tIdXdPTFhDR2dQa2N2YWRmTnZSTDF5V1NkcjNhZGd3ZTB3bzMvTjFWMFNuMUtZMXQ2aGJsMlVVQzRKRG8veENaRTNkMWc2b0ZDT2FPbm9DVm9IV3dReU9tK0J0WlVqUHJLaS9nazBDMytGUlk4ZkVOeWhaelFTQ3pYaG1OeWI3ZmdUdVRnais4RUVWb2JQb3JnT2RCZEcxQkdGWkpsQ2lEMk55aFpyKy9uOUhybUR2QXRtQ1NkNE02bnlJSXVTSVBENjlxUDhSS0QvSW00R1llTzhoclp5NURybXZvdGRUbjBlcHpoZmZ5RXlNR01LL0VDbHE3NmFncmN3Yk9uKzZyM1NvUVlpcnA1V3E4VU9rSVBXVTYzUEhSZldMeEY5ak1hN1MvUzllMmtVSnVUUyszcWFDTWdiZkN3dzlsR2NNSTFNZ2lscittWnJ3VnlyeWxRVVdKTDVDbEhGQ1VpYyttblh1cg===="
    url2 = "https://www.cleverbridge.com/1533/surl-7tWud8SsiC"
    decrypt_url((url2.split("eurl="))[1])