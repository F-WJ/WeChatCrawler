# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2018 / 1 / 9
import requests

def crawl():
    url = "https://mp.weixin.qq.com/mp/profile_ext" \
          "?action=home" \
          "&__biz=MjM5MzgyODQxMQ==" \
          "&scene=124&devicetype=android-24" \
          "&version=26060133&lang=zh_CN" \
          "&nettype=WIFI&a8scene=3" \
          "&pass_ticket=9%2F6LknoxSlydxsdNc5ecV9AmhvAln77E5CSdIKk" \
          "%2BZoSh7xDCXPx6RXPty5pMV7Vz" \
          "&wx_header=1"
    headers = '''
Host: mp.weixin.qq.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Linux; Android 7.0; Mi Note 2 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN
x-wechat-key: b688559d6ff3fbed5f568a66c255605b802c7416d6ebfe6fb912fd15727175ce2122c77203eed3b1a5cf944a11a8abb83aa6301792112b910ac6a895f70958c3b1dcd63262b377c9150cf684e9d62cb2
x-wechat-uin: MjA3Njc0MTAwMQ%3D%3D
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: sd_userid=18861489362350793; sd_cookie_crttime=1489362350793; tvfe_boss_uuid=2e9655075626eb61; RK=CaObR3LaR5; gid=82fdcd05-0c3d-415b-bcdd-87cbe92d7cc4; pgv_pvi=2601810944; pac_uid=0_932f1aa5f4e35; ua_id=kE9kVdDwMCCFio0aAAAAAOmF24i23FqG2pg7TGWEqiQ=; ptcz=20c41fc2cfc570cec0dcf5cf052e240af82cfe5b2839f4ae1280b7e3d71a81cb; pt2gguin=o0364580936; o_cookie=364580936; pgv_info=ssid=s8661899716; pgv_pvid=8564607811; rewardsn=; wxtokenkey=1b4b4cc1cc996b041169867e8f0f78484f3dfb484ccbccf73ddfd65ab59824c0; wxuin=2076741001; devicetype=android-24; version=26060133; lang=zh_CN; pass_ticket=9/6LknoxSlydxsdNc5ecV9AmhvAln77E5CSdIKk+ZoSh7xDCXPx6RXPty5pMV7Vz; wap_sid2=CImbot4HEnA0SzhiM2tDQVJTVlNtU1BqTXZyVFg0UFVlVXdPemotT2ZnUExGbnVMNkxfOFZQdXpvMXNmSlVuNlBrSlFnZUhLUEY5d3lBMFFkeFZINDZ6Rlk0R1RKdVZhSHJRYlRpSkFxWElXWU9ETUJFU3JBd0FBMIOm5tIFOA1AlU4=
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.1&TBSVC=43602&CO=BK&COVC=043807&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MiNote2 &RL=1080*1920&OS=7.0&API=24
Q-GUID: 2af3a0dfa8f770bff552a88a13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
'''
    headers = headers_to_dict(headers)
    # 将 verify 设置为 False，Requests 也能忽略对 SSL 证书的验证。
    response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    with open("weixin_history.html", "w", encoding="utf-8") as f:
        f.write(response.text)
    extract_data(response.text)


# 将请求头转换成字典
def headers_to_dict(headers):
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


def extract_data(html_content):
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data1 = match.group(1)
        # 反转义 unescape
        data2 = html.unescape(data1)
        data3 = json.loads(data2)
        articles = data3.get("list")
        for item in articles:
            print(item)
        return articles

if __name__=="__main__":
    cd = crawl()








































# HTTP/1.1 200 OK
# RetKey: 14
# LogicRet: 0
# Content-Type: text/html; charset=UTF-8
# Cache-Control: no-cache, must-revalidate
# Set-Cookie: wxuin=2076741001; Path=/; HttpOnly
# Set-Cookie: devicetype=android-24; Path=/
# Set-Cookie: version=26060133; Path=/
# Set-Cookie: lang=zh_CN; Path=/
# Set-Cookie: pass_ticket=ahUqlGJ9QmSMAse/pXN3dZWvgA2KJCF36FyqnsE+vYVnwsJ0lEj494ecSXoxryI1; Path=/; HttpOnly
# Set-Cookie: wap_sid2=CImbot4HElwycVVrMjhBeTVyV2pFS0NVLTRuTzVfVDlSRFFKRGhHdkZoMFRpRzBick1PZ1l3dV8tcjB5d0Uza2lCUlZoZDJ5M1lEcDYzNUtHeENidWlaSW1JNFoxYW9EQUFBfjCC5tHSBTgMQJRO; Path=/; HttpOnly
# Connection: keep-alive
# Content-Length: 27984


