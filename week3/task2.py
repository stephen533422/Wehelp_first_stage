import urllib.request as req
import bs4
url="http://www.ptt.cc/bbs/movie/index.html"
request=req.Request(url, headers={
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")
with open("movie.txt", "w", newline="") as file:
    for title in titles:
        if title.a!=None:
            file.write(title.a.string+",")
            # print(title.a.string)
            # print(title.a["href"])
            items=title.find_previous_sibling("div", class_="nrec")
            for item in items:
                # print(item)
                tweet=item.get_text()
                file.write(tweet+",")
                # print(tweet)
            url="https://www.ptt.cc"+title.a["href"]
            request=req.Request(url, headers={
            "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            })
            with req.urlopen(request) as response:
                data=response.read().decode("utf-8")
            root2=bs4.BeautifulSoup(data, "html.parser")
            items=root2.find_all("div", class_="article-metaline")
            for item in items:
                # print(time)
                if item.span.string=="時間":
                    times=item.span.find_next_siblings("span", class_="article-meta-value")
                    for i in times:
                        time=i.get_text()
                        file.write(time+"\n")
                        # print(time)
        

