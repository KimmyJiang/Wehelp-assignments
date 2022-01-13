import urllib.request as request
import json

# 台北市政府景點公開資料
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"


with request.urlopen(src) as response:
    data=json.load(response)["result"]["results"]

with open("data.csv","w",encoding="utf-8") as file:
    
    for i in data:
        
        # 景點名稱
        stitle = i["stitle"]

        # 區域
        address = i["address"]
        value = address.index("區")
        region = address[value-2:value+1]

        # 經度
        longitude = i["longitude"]

        # 緯度
        latitude = i["latitude"]

        #第一張圖檔網址
        photo = i["file"].split("https://")
        photo = "https://" + photo[1]

        file.write(stitle + "," + region + "," + longitude + "," + latitude + "," + photo + "\n" )
