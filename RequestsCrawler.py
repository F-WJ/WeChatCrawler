import requests
'''get请求'''
r = requests.get("https://httpbin.org/ip")
# 响应对象
print(r)
# 响应状态码
print(r.status_code) 
# 响应内容
print(r.content) 

'''POST请求'''
r = requests.post('http://httpbin.org/post', data={'key':'value'})
print(r.content)

'''自定义请求头'''
url = 'https://httpbin.org/headers'
headers = {'user-agetn': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)


'''参数传递'''
url = "http://httpbin.org/get"
r = requests.get(url, params={"key":"val","1":"2"})
print(r.url)


'''指定Cookie'''
s = requests.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
s.text


'''设置超时'''
r = requests.get('https://google.com', timeout=5)


'''设置代理'''
proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}

r = requests.get('http://www.kuaidaili.com/free/', proxies=proxies, timeout=2)



'''
Session
如果想和服务器一直保持登录（会话）状态，而不必每次都指定 cookies，
那么可以使用 session，Session 提供的API和 requests 是一样的。
'''
s = requests.Session()
s.cookies = requests.utils.cookiejar_from_dict({"a":"c"})
r = s.get('http://httpbin.org/cookies')
print(r.text)

r = s.get('http://httpbin.org/cookies')
print(r.text)
