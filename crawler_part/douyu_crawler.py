import time

import requests


class DouYu(object):

    def __init__(self):
        self.url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'
        self.page = 1
        self.num = 1
        self.flag = 1

    def __get_response(self):  # 请求接口，返回响应
        res = requests.get(self.url+str(self.page))
        response = res.json()
        return response

    def __get_first_name(self):  # 拿到第一页第一个的主播姓名，用来判断循环重复
        url = 'https://www.douyu.com/gapi/rkc/directory/0_0/1'
        res = requests.get(url)
        response = res.json()
        first_name = response['data']['rl'][0]['nn']
        return first_name

    def crawl(self):
        first_name = self.__get_first_name()  # 得到当前排名第一个主播姓名，用来判断循环结束
        str_people = ''
        str_popular = ''

        while DouYu.flag == 1:
            if self.page > 100:
                break
            response = self.__get_response()
            info = response['data']['rl']
            for i in range(len(info)):
                name = info[i]['nn']
                temp = info[i]['c2name']
                if len(temp) == 0:
                    temp = 'null'
                game = ''
                for j in range(len(temp)):
                    if temp[j] not in [' ', ':']:
                        game += temp[j]
                hot = int(info[i]['ol'])
                if self.num > 300:
                    if first_name == name:
                        self.flag = 0
                        break
                self.num += 1  # 计算直播数量
                print("{}.主播姓名:{}, 人气:{:,},直播类型:{}".format(self.num, name, hot, game))
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
        self.flag = 1


if __name__ == '__main__':
    DouYu = DouYu()
    while True:
        DouYu.crawl()
        time.sleep(30)
