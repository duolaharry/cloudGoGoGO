import time
import requests


class DouYu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'
        self.page = 1  # 当前已爬取页数
        self.num = 1  # 当前已爬取直播间数

    def __get_response(self):  # 请求接口，返回响应
        response = requests.get(self.url+str(self.page))
        res = response.json()
        return res

    def crawl(self):
        str_people = ''
        str_popular = ''
        while True:
            if self.page > 100:
                break
            response = self.__get_response()
            info = response['data']['rl']
            for i in range(len(info)):
                name = info[i]['nn']  # 直播间名
                hot = int(info[i]['ol'])  # 热度

                # 规范化直播类型名，删掉直播类型中的空格和冒号，如果直播类型为空则设置为"null"
                temp = info[i]['c2name']
                if len(temp) == 0:
                    temp = 'null'
                game = ''
                for j in range(len(temp)):
                    if temp[j] not in [' ', ':']:
                        game += temp[j]
                # ----

                self.num += 1  # 计算直播数量
                print("{}.主播姓名:{}  人气:{:,}  直播类型:{}".format(self.num, name, hot, game))
                str_people += 'name:{} num:1\n'.format(game)
                str_popular += 'name:{} num:{}\n'.format(game, hot)
            self.page += 1
            print('第{}页完结'.format(DouYu.page))
        with open('./Long/douyu/people.txt', 'w') as file_people:
            file_people.write(str_people[0: len(str_people) - 1])
        with open('./Long/douyu/popular.txt', 'w') as file_popular:
            file_popular.write(str_popular[0: len(str_popular) - 1])
        print('\n牛牛')
        self.page = 1
        self.num = 1


if __name__ == '__main__':
    DouYu = DouYu()
    while True:
        DouYu.crawl()
        time.sleep(30)
