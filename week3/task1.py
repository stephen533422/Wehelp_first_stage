import urllib.request as req
import json
import csv
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"

request=req.Request(url, headers={
    "Content-Type":"application/json",
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    result = response.read().decode("utf-8")
data=json.loads(result)
district = [ "中正區", "萬華區", "中山區", "大同區", "大安區" ,"松山區", "信義區", "士林區", "文山區", "北投區", "內湖區", "南港區"]
mrt_list = {}

items = data["result"]["results"]

with open("attraction.csv", mode="w", newline="") as file:
    writer=csv.writer(file)
    for item in items:
        if item["address"][5:8] in district:
            writer.writerow([item["stitle"],item["address"][5:8],item["longitude"],item["latitude"],item["file"]])

with open("MRT.csv", mode="w", newline="")as file:
    writer = csv.writer(file)

    for item in items:
        str = item["MRT"]
        tag = False
        for key in mrt_list:
            if(key==str):
                mrt_list[key].append(item["stitle"])
                tag=True
        if(tag==False):
            mrt_list.update( {str: [item["stitle"]]})

    for i in mrt_list:
        write_list=[]
        write_list.append(i)
        for j in mrt_list[i]:
            write_list.append(j)
        writer.writerow(write_list)
