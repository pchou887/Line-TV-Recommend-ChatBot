import requests as req
from bs4 import BeautifulSoup
import json

res = req.get("https://www.linetv.tw/")
soup = BeautifulSoup(res.text)

j = json.loads(soup.find("script").text[27:])
c = 0
bk = 0
for search in j['ssrData']['https://api.linetv.tw/v2/index']:
    if search["title"] == "熱播排行榜":
        for d in search["datas"]:
            print("https://www.linetv.tw/drama/"+ str(d["data"]["id"])) #網址
            print(d["data"]["posterUrl"]) #圖片網址
            print(d["data"]["name"]) #劇名
            c += 1
            if c == 10:
                bk = 1
                break
    elif bk == 1:
        break
count = 0
for i in j_d["data"]:
    count += 1
    print(count)
    temp = []
    temp_y = []
    temp.append("https://www.linetv.tw/drama/" + str(i["contentId"])) #劇網址
    if "\t" in i["name"]:
        temp.append(i["name"].replace('\t', ' '))
    elif "\xa0" in i["name"]:
        temp.append(i["name"].replace('\xa0', ' '))
    else:
        temp.append(i["name"]) #劇名
    temp.append(i["authorizedStartAt"]) #認證起始時間
    temp.append(i["authorizedEndAt"]) #認證結束時間
    temp.append(i["publishedStartAt"]) #平台推出時間
    temp.append(i["publishedEndAt"]) #平台結束時間
    temp.append(i["viewCount"]['total']) #觀看次數(不確定)
    temp.append(i["viewCount"]['last7Days']) #觀看次數(不確定)
    temp.append(round(i["userRatingAvg"], 2)) #評分
    temp.append(i["userRatingCount"]) #評分人數
    temp.append(i["contentRating"]["name"]) #分級
    temp.append(i["contentRating"]["minAge"]) #最小年紀
    for t in i["genre"]:
        if t["key"] == "愛情":
            for t in i["genre"]:
                if t["id"] >= 382 and t["id"] <= 392:
                    temp_y.append(t["key"])
            for t in i["genre"]:
                if t["id"] == 417 or t["id"] == 374:
                    temp_y.append(t["key"])
            break
    
    for t in temp:
        if len(temp) == 2:
            break
        elif len(temp) == 1:
            temp_y.append("")
        elif len(temp) == 3:
            temp_y.pop(0)
    for t in temp_y:
        temp.append(t)
#     for t in i["genre"]:
#         if not (t["id"] >= 382 and t["id"] <= 417 or t["id"] == 374 or t["id"] == 494):
#             if "\x08" in t["key"]:
#                 temp.append(t["key"].replace('\x08', ''))
#             else:
#                 temp.append(t["key"])