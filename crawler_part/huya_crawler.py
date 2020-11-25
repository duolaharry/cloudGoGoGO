import requests
import json

file_people = open('./Long/huya/people.txt', 'w')
file_popular = open('./Long/huya/popular.txt', 'w')
page, count, num = 1, 0, 0
url = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page="

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
        file_people.write('name:{} num:1\n'.format(gamename))
        file_popular.write('name:{} num:{}\n'.format(gamename, totalCount))
    print("第%s页结束" % page)
    page += 1

file_people.close()
file_popular.close()
