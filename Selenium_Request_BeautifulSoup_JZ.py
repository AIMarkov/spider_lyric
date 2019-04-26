#selenuim+BeautifulSoup实现
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
##为什么用S+R+B,因为页面是动态,先用selenium动态获取信息,用BeautifulSoup来解析.最后下载使用Requests，这是因为Selenium需要加载页面,而requests不需要


driver=webdriver.Firefox()
url_init="http://music.taihe.com/artist/7994?pst=sug"
driver.get(url_init)
page_list=list(range(2,27))
file=open("JZID_Name1.csv","w")
writer=csv.writer(file)


def B_get_song_id(page,text):

    soup=BeautifulSoup(text,"html.parser")
    print("page:",page)
    if page==0:
        songs = soup.find_all("a", "songlist-songname")
    else:
        songs=soup.find_all("a","namelink gray")
    song=[]
    for a in songs:
        song_inf={}
        song_inf["name"]=a["title"]
        song_inf["id"]=a["href"].split("/")[-1]
        song.append(song_inf)
    print(song)
    return song



def S_get_page(driver):
    songs=[]
    data=B_get_song_id(0,driver.page_source)

    songs.extend(data)
    for page_num in page_list:
        a_list=driver.find_elements_by_css_selector("a.page-navigator-number")
        for a in a_list:
            if int(a.text)==page_num:
                 page=int(a.text)
                 a.click()
                 time.sleep(10)#加载时间，保证加载完成
                 data=B_get_song_id(page,driver.page_source)
                 songs.extend(data)
                 break
    return songs

data=S_get_page(driver)
for song in data:
    writer.writerow(song.values())
file.close()
driver.close()

#如过文件"ID_Name.txt"或者"ID_Name.csv"存在,将上面语句注释,我们直接执行下面语句
import pandas as pd


def R_get_text(url):
    try:
        print("url:",url)
        Response=requests.get(url)
        Response.raise_for_status()
        Response.encoding=Response.apparent_encoding
        return Response.text
    except:
        print("出现错误再Try一次")
        try:
            print("url:", url)
            Response = requests.get(url)
            Response.raise_for_status()
            Response.encoding = Response.apparent_encoding
            return Response.text
        except:
            print("出现错误")
            print("错误地点：", url)
            return None

def B_get_lrc_link(text):
    soup=BeautifulSoup(text,"html.parser")
    lrcbox=soup.find("div","lrc-list")
    if lrcbox:
        return lrcbox["data-lrclink"]


def get_lrc_link_list(data,url):
    lrc_links=[]
    for ip in data["IP"]:
        id_link={}
        text=R_get_text(url+str(ip))
        time.sleep(3)
        if text:##如果不为空就写入
            id_link["Link"]=B_get_lrc_link(text)
            id_link["IP"]=str(ip)
            lrc_links.append(id_link)
    return lrc_links

def get_lrc(linklist,path):
    for ip_link in linklist:
        with open(path+ip_link["IP"]+".txt","w") as f:
            lrc=R_get_text(ip_link["Link"])
            if lrc:
                f.write(lrc)



def main():
    data = pd.read_csv("JZID_Name1.csv", names=["Name", "IP"])
    url = "http://music.taihe.com/song/"
    save_path = "ZJLyrcFile/"
    lrc_links=get_lrc_link_list(data,url)
    get_lrc(lrc_links,save_path)

main()
