import requests
from bs4 import BeautifulSoup
#A方案:刚开始是想直接在千千音乐上搜索:周杰伦 歌词,每个页面有二十首,但是不全是周杰伦的且有重复,
#而且爬去时发现格式太乱,因此放弃这种方案
#B方案:这里我们换取爬去路径,搜索:周杰伦,然后出现歌曲列表没有直接出现歌词,
# 由于是动态网页爬去,所以我们分析爬去方案,我们通过分析可以知道每首歌的单独界面是http://music.taihe.com/song/+代号,因此,我们可以先在歌曲列表界面获取周杰伦歌的所有代号
#然后再通过代号进入单个歌曲界面,再获取歌词,此时歌词是lric文件




#首先获取歌曲代号
def get_url(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        response.encoding=response.apparent_encoding
        return response.text
    except:
        print("爬去失误")

def get_lyrc_url(text):
    soup=BeautifulSoup(text,"html.parser")
    print(soup.find_all("div","page-inner"))
url="http://music.taihe.com/artist/7994?pst=sug"
text=get_url(url)
get_lyrc_url(text)
