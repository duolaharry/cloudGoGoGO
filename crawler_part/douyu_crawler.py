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
        file_people = open('./Long/douyu/people.txt', 'w')
        file_popular = open('./Long/douyu/popular.txt', 'w')

        while DouYu.flag == 1:
            response = self.__get_response()
            self.info = response['data']['rl']
            for i in range(len(self.info)):
                self.info = response['data']['rl']
                name = self.info[i]['nn']
                game = self.info[i]['c2name']
                hot = int(self.info[i]['ol'])
                if self.num > 300:
                    if first_name == name:
                        self.flag = 0
                        break
                self.num += 1  # 计算直播数量
                print("{}.主播姓名:{}, 人气:{:,},直播类型:{}".format(self.num, name, hot, game))
                file_people.write('name:{} num:1\n'.format(game))
                file_popular.write('name:{} num:{}\n'.format(game, hot))
            DouYu.page += 1
            print('第{}页完结'.format(DouYu.page))
        file_people.close()
        file_popular.close()


if __name__ == '__main__':
    DouYu = DouYu()
    DouYu.crawl()
