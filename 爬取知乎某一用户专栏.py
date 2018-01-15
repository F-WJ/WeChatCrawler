import json
import requests


class SimplerCrawler:
    # 爬取地址
    init_url = "https://zhuanlan.zhihu.com/api/columns/pythoneer/followers"
    offset = 0

    def crawl(self, params=None):
        headers = {
            "Host": "zhuanlan.zhihu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        response = requests.get(self.init_url, headers=headers, params=params)
        print(response.url)
        data = response.json()

        # 7000表示所有关注量
        while self.offset < 7000:
            self.parse(data)
            self.offset += 20
            params = {"limit":20,"offset":self.offset}
            self.crawl(params)

    def parse(self, data):
        # 以json格式存储文件
        with open("followers.json", "a", encoding="utf-8") as f:
            for item in data:
                # ensure_ascii 参数 中文编码
                # 中文编码问题资料：http://www.cnblogs.com/biangbiang/archive/2013/02/19/2916780.html
                f.write(json.dumps(item,ensure_ascii = False))
                f.write('\n')

if __name__ == '__main__':
    SimplerCrawler().crawl()
        
