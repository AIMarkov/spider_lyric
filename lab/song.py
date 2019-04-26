import requests
from bs4 import BeautifulSoup
import re
url="http://music.taihe.com/search/lrc?key=%E5%91%A8%E6%9D%B0%E4%BC%A6%20%E6%AD%8C%E8%AF%8D"
def get_text(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        return response.text
    except:
        print("爬取失败")
text=get_text(url)
soup=BeautifulSoup(text,"html.parser")
#print(soup)
# print(soup.title)
# print(soup.a.string)
data=[]
def get_lyric(text):
    soup=BeautifulSoup(text,"html.parser")
    content=soup.find_all("div","lrc-content")
    for div in content:
        p=div.find(name="p")
        #print(p)
        song=p.text
        song=song.split("\n")
        print(song)
        #Song={}

        #Song["name"]=song[0]
        # Song["lyricist"]=song[1].split("：")[1]
        # Song["lyric"]=song[4:]
        # data.append(Song)


get_lyric(text)