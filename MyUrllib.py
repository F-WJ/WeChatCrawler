# urllib模块使用
import ssl

from urllib.request import Request
from urllib.request import urlopen

# 解决访问Https时不受信任SSL证书问题
context = ssl._create_unverified_context()
# HTTP请求
request = Request(  url="https://foofish.net/pip.html",
                    method="GET",
                    headers={"HOST":"footfish.net"},
                    data=None)


# HTTP响应
response = urlopen(request,context=context)
headers = response.info() # 响应头
content = response.read() # 响应头
code = response.getcode() # 状态码
