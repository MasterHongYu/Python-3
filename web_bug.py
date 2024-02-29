#1. 抓取特定網址的資料
import urllib.request as req
#1.1 觀察想要抓取的網頁，取得網址
url = 'https://www.ptt.cc/bbs/shinkai/index.html'
#1.2 利用開發人員工具，觀察網路連線細節 (Request Headers)
request = req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
})
#1.3 建立 Request 物件，附加 Request Headers 設定。
with req.urlopen(request) as response :
    data = response.read().decode("utf-8")

#2. 解析 HTML 格式資料
#2.1 利用 BeautifulSoup 解析並取得資料
import bs4
root=bs4.BeautifulSoup(data,"html.parser")
print(root.title.string)
titles = root.find_all("div",class_="title")
for title in titles :
    if title.a != None :
        print(title.a.string)