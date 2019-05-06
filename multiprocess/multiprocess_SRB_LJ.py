from multiprocessing import Process,Queue#后面这个Queue只能在
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

class Crawler(Process):
    def __init__(self,url_queue,path):
        super(Crawler, self).__init__()
        self.url_queue=url_queue
        self.path=path
    def R_get_text(self,url):
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

    def B_get_lrc_link(self,text):
        soup=BeautifulSoup(text,"html.parser")
        lrcbox=soup.find("div","lrc-list")
        if lrcbox:
            return lrcbox["data-lrclink"]


    def get_lrc_link_list(self):
        lrc_links=[]
        while True:
            id_link={}
            if self.url_queue.empty():
                break
            value=self.url_queue.get()
            text = self.R_get_text(value[0])
            time.sleep(3)
            if text:##如果不为空就写入
                id_link["Link"]=self.B_get_lrc_link(text)
                id_link["IP"]=str(value[1])
                lrc_links.append(id_link)
        return lrc_links

    def get_lrc(self,linklist):
        for ip_link in linklist:
            with open(self.path+ip_link["IP"]+".txt","w") as f:
                lrc=self.R_get_text(ip_link["Link"])
                if lrc:
                    f.write(lrc)
    def run(self):
        lrc_links=self.get_lrc_link_list()
        self.get_lrc(lrc_links)




def main():
    url_queue=Queue(500)
    data = pd.read_csv("LJID_Name1.csv", names=["IP", "Name"])
    url = "http://music.taihe.com/song/"
    save_path = "data/"
    for IP in data["IP"]:
        url_queue.put((url+str(IP),IP))
    process=[]
    for p in range(8):
        process.append(Crawler(url_queue,save_path))
    for p in process:
        p.start()
    for p in process:
        p.join()

a=time.time()
main()
b=time.time()
print("time:",b-a)#133.2544s