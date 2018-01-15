# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2018 / 1 / 13

import logging
import utils
import requests
import time
import json
from datetime import datetime
import html

from models import Post

from requests.packages import urllib3

urllib3.disable_warnings()
from urllib.parse import urlsplit

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WeiXinCrawer:
    def crawl(self, offset=0):

        # 如果运行失败，请修改url某些关键值和headers，下面有对比
        url = "https://mp.weixin.qq.com/mp/profile_ext?" \
              "action=getmsg&" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "f=json&" \
              "offset={offset}&" \
              "count=10&" \
              "is_ok=1&" \
              "scene=124&" \
              "uin=777&" \
              "key=777&" \
              "pass_ticket=IlqxjPEmgZu1FF%2BoLPoEacmQD%2Bpo%2BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&wxtoken=&" \
              "appmsg_token=939_hihttu0x83ppBkaiAcL5WMcghKBKviEePk53yg~~&x5=1&f=json".format(offset=offset)

        url2 = "https://mp.weixin.qq.com/mp/profile_ext?" \
               "action=getmsg&" \
               "__biz=MjM5MzgyODQxMQ==&" \
               "f=json&" \
               "offset={offset}&" \
               "count=10&" \
               "is_ok=1&" \
               "scene=124&" \
               "uin=777&key=777&" \
               "pass_ticket=IlqxjPEmgZu1FF%" \
               "2BoLPoEacmQD%" \
               "2Bpo%2BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&wxtoken=&" \
               "appmsg_token=939_oSn%" \
               "252BfxCfRbQkDYBJvf52NedMZCifsAekP2Am7g~~&" \
               "x5=1&f=json".format(offset=offset)

        url1 = "https://mp.weixin.qq.com/mp/profile_ext?" \
               "action=getmsg&" \
               "__biz=MjM5MzgyODQxMQ==&" \
               "f=json&" \
               "offset={offset}&" \
               "count=10&is_ok=1&" \
               "scene=124&" \
               "uin=777&key=777&" \
               "pass_ticket=9%" \
               "2F6LknoxSlydxsdNc5ecV9AmhvAln77E5CSdIKk%2BZoSh7xDCXPx6RXPty5pMV7Vz&wxtoken=&" \
               "appmsg_token=939_5uFg4avbgDmzVEO0qQT_gALmbvliqJeaQDCp4g~~&" \
               "x5=1&" \
               "f=json".format(offset=offset)

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 7.0; Mi Note 2 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN
Accept: */*
Referer: https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzgyODQxMQ==&scene=124&devicetype=android-24&version=26060135&lang=zh_CN&nettype=WIFI&a8scene=3&pass_ticket=IlqxjPEmgZu1FF%2BoLPoEacmQD%2Bpo%2BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: sd_userid=18861489362350793; sd_cookie_crttime=1489362350793; tvfe_boss_uuid=2e9655075626eb61; RK=CaObR3LaR5; gid=82fdcd05-0c3d-415b-bcdd-87cbe92d7cc4; pgv_pvi=2601810944; pac_uid=0_932f1aa5f4e35; ua_id=kE9kVdDwMCCFio0aAAAAAOmF24i23FqG2pg7TGWEqiQ=; ptcz=20c41fc2cfc570cec0dcf5cf052e240af82cfe5b2839f4ae1280b7e3d71a81cb; pt2gguin=o0364580936; o_cookie=364580936; pgv_pvid=8564607811; rewardsn=; wxtokenkey=40c4e47bfcfbdb3be81209fce95dd5ac82cb3adacf5b6b224f97bba30c96dabb; wxuin=2076741001; devicetype=android-24; version=26060135; lang=zh_CN; pass_ticket=IlqxjPEmgZu1FF+oLPoEacmQD+po+SAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy; wap_sid2=CImbot4HElxoZThTLWNjNnBYUHcxMHU1c2ROU21SalFmSHl3ajlrczNJRU5UVVJfUDNjeEtaZVVqbDBYTTlqU2xTVVpqcXB5cGdUOGlSS3c1RUpMX2lMQ21QNk1nS3NEQUFBfjCu0vHSBTgMQJRO
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.1&TBSVC=43602&CO=BK&COVC=043807&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MiNote2 &RL=1080*1920&OS=7.0&API=24
Q-GUID: 2af3a0dfa8f770bff552a88a13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
"""
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
            # 保存文章数据
            self.save(msg_list)
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                # 递归
                next_offset = result.get("next_offset")
                time.sleep(2)
                self.crawl(next_offset)
        else:
            # 错误消息
            logging.error("无法正确获得内容")
            exit()

    # 保存所有文章到mongodb
    @staticmethod
    def save(msg_list):
        # 将http:\/\/中的\/,修改为/
        # 文档：http://blog.csdn.net/zcmlimi/article/details/47709049
        msg_list = msg_list.replace("\/", "/")
        data = json.loads(msg_list)
        msg_list = data.get("list")
        for msg in msg_list:
            p_date = msg.get("comm_msg_info").get("datetime")
            # 通过app_msg_ext_info值可以检查是否存在内容
            msg_info = msg.get("app_msg_ext_info")
            if msg_info:
                WeiXinCrawer._insert(msg_info, p_date)
                multi_msg_info = msg_info.get("multi_app_msg_item_list")
                for msg_item in multi_msg_info:
                    WeiXinCrawer._insert(msg_item, p_date)
            else:
                logging.warning(u"文章不存在， data=%s" % json.dumps(msg.get("comm_msg_info")))

    # 文章下载
    # staticmethod静态方法说明：http://blog.csdn.net/youngbit007/article/details/68957848
    @staticmethod
    def _insert(item, p_date):
        keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
        # 过滤无用字段
        sub_data = utils.sub_dict(item, keys)
        post = Post(**sub_data)
        # 日期转换
        # 资料：http://www.wklken.me/posts/2015/03/03/python-base-datetime.html
        p_date = datetime.fromtimestamp(p_date)
        post["p_date"] = p_date
        # 打印信息
        logger.info('save data %s' % post.title)
        try:
            post.save()
        except Exception as e:
            logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)

    # 获取文章阅读量，点赞数，评论数，赞赏数
    @staticmethod
    def update_post(post):
        # 文章url参数
        # title参数不用管，没有影响
        data_url_params_url = "__biz=MjM5MzgyODQxMQ==&" \
                              "appmsg_type=9&" \
                              "mid=2650367799&" \
                              "sn=afd47703d8bfd41f547c3916a25a4922&" \
                              "idx=1&" \
                              "scene=38&" \
                              "title=%E6%8E%A8%E8%8D%90%E5%87%A0%E4%B8%AA%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%88%E6%96%87%E6%9C%AB%E5%BD%A9%E8%9B%8B%EF%BC%89&" \
                              "ct=1515730434&" \
                              "abtest_cookie=BAABAAgACgAMAA0ACgCehh4AlYoeAKCKHgCxih4AuooeAL+KHgDGih4AyooeANiKHgDdih4AAAA=&devicetype=android-24&" \
                              "version=/mmbizwap/zh_CN/htmledition/js/appmsg/index3b1748.js&" \
                              "f=json&" \
                              "r=0.32110940912764097&" \
                              "is_need_ad=1&" \
                              "comment_id=4119591256&" \
                              "is_need_reward=0&" \
                              "both_ad=0&" \
                              "reward_uin_count=0&" \
                              "msg_daily_idx=1&" \
                              "is_original=0&" \
                              "uin=777&" \
                              "key=777&" \
                              "pass_ticket=IlqxjPEmgZu1FF%25252BoLPoEacmQD%25252Bpo%25252BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&" \
                              "wxtoken=1044847233&devicetype=android-24&" \
                              "clientversion=26060135&" \
                              "appmsg_token=939_faosuyskmbgJ7K6WTQdsnO_RZ5I4iaY5qFSIpAp9fCvhtU1OKrI8rZ2vJHTu_c40JGJqPPbMvqn-UG1p&" \
                              "x5=1&f=json"

        data_url_params = utils.str_to_dict(data_url_params_url, "&", "=")
        # url转义处理，文档：https://www.cnblogs.com/xuxn/archive/2011/08/12/parse-html-escape-characters-in-python.html
        content_url = html.unescape(post.content_url)
        # 分拆url,提取query的信息，资料地址：http://blog.51cto.com/yucanghai/1695439
        content_url_params = urlsplit(content_url).query
        # 将参数转化为字典
        content_url_params = utils.str_to_dict(content_url_params, "&", "=")
        # 使用字典update方法，更新文章url的参数
        data_url_params.update(content_url_params)
        body = "is_only_read=1&" \
               "req_id=03230SZyTR8kQlPVkKwxbt1A&" \
               "pass_ticket=mXHYjLnkYux1rXx8BxNrZpgW4W%25252ByLZxcuvpDWlxbBrjvJo3ECB%25252BckDAsy%25252FTJJK6P&" \
               "is_temp_url=0"

        # 将body的值转化为字典
        data = utils.str_to_dict(body, "&", "=")

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
Content-Length: 155
Origin: https://mp.weixin.qq.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 7.0; Mi Note 2 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650367799&idx=1&sn=afd47703d8bfd41f547c3916a25a4922&chksm=be9cdc6389eb5575f75e424c2351969e3d6b066cb1d60466d4865381f8de5d41867ca2a526b1&scene=38&ascene=0&devicetype=android-24&version=26060135&nettype=WIFI&abtest_cookie=BAABAAgACgAMAA0ACgCehh4AlYoeAKCKHgCxih4AuooeAL%2BKHgDGih4AyooeANiKHgDdih4AAAA%3D&lang=zh_CN&pass_ticket=IlqxjPEmgZu1FF%2BoLPoEacmQD%2Bpo%2BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: sd_userid=18861489362350793; sd_cookie_crttime=1489362350793; tvfe_boss_uuid=2e9655075626eb61; RK=CaObR3LaR5; gid=82fdcd05-0c3d-415b-bcdd-87cbe92d7cc4; pgv_pvi=2601810944; pac_uid=0_932f1aa5f4e35; ua_id=kE9kVdDwMCCFio0aAAAAAOmF24i23FqG2pg7TGWEqiQ=; ptcz=20c41fc2cfc570cec0dcf5cf052e240af82cfe5b2839f4ae1280b7e3d71a81cb; pt2gguin=o0364580936; o_cookie=364580936; pgv_pvid=8564607811; rewardsn=; wxtokenkey=90c34bc971c6ce5a8df3de87ab70143e0d6711e65604c5feedb0b6b425311912; wxuin=2076741001; devicetype=android-24; version=26060135; lang=zh_CN; pass_ticket=IlqxjPEmgZu1FF+oLPoEacmQD+po+SAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy; wap_sid2=CImbot4HElw4RE5GUGcyWFFQV1drdFJ5cXpZMG5yMm9qWWtwZFRoQml0TFZUVnpXVGU1RThIS3hJejhsSzFZUWw3cTdGbXVjTTdWZkpVVGVNTmhCR3l3U2FBMURGYXNEQUFBfjCzw/HSBTgNQAE=
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.1&TBSVC=43602&CO=BK&COVC=043807&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= MiNote2 &RL=1080*1920&OS=7.0&API=24
Q-GUID: 2af3a0dfa8f770bff552a88a13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b      
"""
        headers = utils.str_to_dict(headers)
        # 文章url
        data_url = "https://mp.weixin.qq.com/mp/getappmsgext"
        r = requests.post(data_url, data=data, verify=False, params=data_url_params, headers=headers)

        # 保存数据
        result = r.json()
        if result.get("appmsgstat"):
            # 阅读数
            post['read_num'] = result.get("appmsgstat").get("read_num")
            # 点赞数
            post['like_num'] = result.get("appmsgstat").get("like_num")
            # 赞赏数
            post['reward_num'] = result.get("appmsgstat").get("reward_total_count")
            #
            post['u_date'] = datetime.now()
            logger.info("%s read_num: %s like_num: %s reward_num: %s" %
                        (post.title, post['read_num'], post['like_num'], post['reward_num']))
            post.save()
        else:
            logger.warning(u"出错")
            exit()


if __name__ == '__main__':
    crawler = WeiXinCrawer()
    # crawler.crawl()
    # 获取点赞数等
    # mongoengine查询使用手册：http://funhacks.net/2016/04/03/mongoengine_%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8/
    for post in Post.objects(reward_num=0):
        crawler.update_post(post)
        time.sleep(1)

# 文章
url3 = "http://mp.weixin.qq.com/s?" \
       "__biz=MjM5MzgyODQxMQ==&" \
       "mid=2650367799&" \
       "idx=1&" \
       "sn=afd47703d8bfd41f547c3916a25a4922&" \
       "chksm=be9cdc6389eb5575f75e424c2351969e3d6b066cb1d60466d4865381f8de5d41867ca2a526b1&" \
       "scene=27"

# 点赞数等信息
data_url = "https://mp.weixin.qq.com/mp/getappmsgext?" \
           "__biz=MjM5MzgyODQxMQ==&" \
           "appmsg_type=9&" \
           "mid=2650367799&" \
           "sn=afd47703d8bfd41f547c3916a25a4922&" \
           "idx=1&" \
           "scene=38&" \
           "title=%E6%8E%A8%E8%8D%90%E5%87%A0%E4%B8%AA%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%88%E6%96%87%E6%9C%AB%E5%BD%A9%E8%9B%8B%EF%BC%89&" \
           "ct=1515730434&" \
           "abtest_cookie=BAABAAgACgAMAA0ACgCehh4AlYoeAKCKHgCxih4AuooeAL+KHgDGih4AyooeANiKHgDdih4AAAA=&" \
           "devicetype=android-24&" \
           "version=/mmbizwap/zh_CN/htmledition/js/appmsg/index3b1748.js&" \
           "f=json&r=0.727572550037541&is_need_ad=0&comment_id=4119591256&" \
           "is_need_reward=0&" \
           "both_ad=0&" \
           "reward_uin_count=0&" \
           "msg_daily_idx=1&" \
           "is_original=0&" \
           "uin=777&" \
           "key=777&" \
           "pass_ticket=IlqxjPEmgZu1FF%25252BoLPoEacmQD%25252Bpo%25252BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&" \
           "wxtoken=3240161557&" \
           "devicetype=android-24&" \
           "clientversion=26060135&" \
           "appmsg_token=939_zv2hxeO8M1b8JNMTTQdsnO_RZ5I4iaY5qFSIpEqAlb4Eel1J5UGYDdsqHhFg-9dW8DWMPFs7smVVkYpp&x5=1&" \
           "f=json"

url33 = "POST https://mp.weixin.qq.com/mp/getappmsgext?" \
        "__biz=MjM5MzgyODQxMQ==&appmsg_type=9&" \
        "mid=2650367799&" \
        "sn=afd47703d8bfd41f547c3916a25a4922&" \
        "idx=1&scene=38&" \
        "title=%E6%8E%A8%E8%8D%90%E5%87%A0%E4%B8%AA%E5%85%AC%E4%BC%97%E5%8F%B7%EF%BC%88%E6%96%87%E6%9C%AB%E5%BD%A9%E8%9B%8B%EF%BC%89&" \
        "ct=1515730434&" \
        "abtest_cookie=BAABAAgACgAMAA0ACgCehh4AlYoeAKCKHgCxih4AuooeAL+KHgDGih4AyooeANiKHgDdih4AAAA=&" \
        "devicetype=android-24&" \
        "version=/mmbizwap/zh_CN/htmledition/js/appmsg/index3b1748.js&" \
        "f=json&r=0.2606427763012864&is_need_ad=1&" \
        "comment_id=4119591256&is_need_reward=0&" \
        "both_ad=0&reward_uin_count=0&msg_daily_idx=1&" \
        "is_original=0&uin=777&key=777&" \
        "pass_ticket=IlqxjPEmgZu1FF%25252BoLPoEacmQD%25252Bpo%25252BSAKlMeJmuJgvxrZqkHisNKGim9X4iizUGDy&" \
        "wxtoken=3064459836&devicetype=android-24&" \
        "clientversion=26060135&" \
        "appmsg_token=939_IrLWdmfGh2S%252B4iABTQdsnO_RZ5I4iaY5qFSIpIClcW128eQExFKyGwudaCkfFMxbllqFDPUPmlCbLkgA&" \
        "x5=1&f=json"
