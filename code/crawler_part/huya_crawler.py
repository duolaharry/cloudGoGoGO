import time
import requests


def run():
    page, num = 1, 0
    url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page="
    str_people = ''
    str_popular = ''

    while True:
        response = requests.get(url + str(page))
        res = response.json()
        artists = res['data']['datas']
        # 如果响应为空的话，代表遍历结束，数据分析打印
        if artists is None or artists == [] or page > 100:
            break

        for i in artists:
            nick = i['nick']  # 直播间名字
            total_count = int(i['totalCount'])  # 人气

            # 规范化直播类型名，删掉直播类型中的空格和冒号，如果直播类型为空则设置为"null"
            temp = i['gameFullName']
            if len(temp) == 0:
                temp = 'null'
            gamename = ''
            for j in range(len(temp)):
                if temp[j] not in [' ', ':']:
                    gamename += temp[j]
            # ----

            num += 1
            print("{}.主播姓名:{}  人气:{:,}  直播类型:{}".format(num, nick, int(total_count), gamename))
            str_people += ('name:{} num:1\n'.format(gamename))
            str_popular += ('name:{} num:{}\n'.format(gamename, total_count))
        print("第%s页结束" % page)
        page += 1

    # 写入
    with open('./Long/huya/people.txt', 'w') as file_people:
        file_people.write(str_people[0: len(str_people) - 1])
    with open('./Long/huya/popular.txt', 'w') as file_popular:
        file_popular.write(str_popular[0: len(str_popular) - 1])
    print('\n牛牛')


if __name__ == '__main__':
    while True:
        run()
        time.sleep(30)
