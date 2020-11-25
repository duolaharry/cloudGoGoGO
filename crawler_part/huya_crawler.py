import requests
import json

page, count, num = 1, 0, 0
url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page="
str_people = ''
str_popular = ''

while True:
    res = requests.get(url+str(page))
    response = res.json()
    artists = response['data']['datas']
    path = './try.json'
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(response, f, indent=2, sort_keys=True, ensure_ascii=False)

    # 如果响应为空的话，代表遍历结束，数据分析打印
    if artists is None or artists == []:
        break

    for i in artists:
        nick = i['nick']
        totalCount = int(i['totalCount'])  # 人气
        gamename = i['gameFullName']
        count += int(totalCount)
        num += 1
        print("{}.主播姓名:{}人气:{:,}".format(num, nick, int(totalCount)))
        str_people += ('name:{} num:1\n'.format(gamename))
        str_popular += ('name:{} num:{}\n'.format(gamename, totalCount))
    print("第%s页结束" % page)
    page += 1

# 写入
with open('./Long/huya/people.txt', 'w') as file_people:
    file_people.write(str_people)
with open('./Long/huya/popular.txt', 'w') as file_popular:
    file_popular.write(str_popular)
