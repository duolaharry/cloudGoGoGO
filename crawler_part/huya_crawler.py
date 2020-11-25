import requests
import time
import json

page, count, num, lis, game_list, hot_list = 1, 0, 0, {}, {}, {}
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
        lis = sorted(lis.items(), key=lambda x: x[1][0], reverse=True)

        # 直播人数
        file = open('./Long/huya/people.txt', 'w')
        game_list = sorted(game_list.items(), key=lambda x: x[1], reverse=True)
        hot_list = sorted(hot_list.items(), key=lambda x: x[1], reverse=True)
        count = 0
        for game in game_list:
            if count >= 10:
                break
            print("name:{} num:{}".format(game[0], game[1]))
            file.write("name:{} num:{}\n".format(game[0], game[1]))
            count += 1
        file.close()
        # ----

        # 分类热度
        file = open('./Long/huya/popular.txt', 'w')
        print("\n当前直播类型人气排名:")
        for hot in range(10):
            print("name:{} num:{}".format(hot_list[hot][0], hot_list[hot][1]))
            file.write("name:{} num:{}\n".format(hot_list[hot][0], hot_list[hot][1]))
        file.close()
        # ----
        break

    for i in artists:
        store = []
        nick = i['nick']
        introduction = i['introduction']
        totalCount = int(i['totalCount'])  # 人气
        gamename = i['gameFullName']
        count += int(totalCount)
        num += 1
        print("{}.主播姓名:{}人气:{:,}".format(num, nick, int(totalCount)))
        store.append(totalCount)
        store.append(gamename)
        lis[nick] = store
        game_list[gamename] = game_list.get(gamename, 0) + 1
        hot_list[gamename] = hot_list.get(gamename, 0) + totalCount
    print("第%s页结束" % page)
    page += 1
