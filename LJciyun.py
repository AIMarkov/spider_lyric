from collections import Counter
import jieba
import os
from wordcloud import  WordCloud
import numpy as np
import matplotlib.pyplot as pl

def chulitext(lrc):
    lrc_pure=[]
    if ("演唱：" in lrc) and ("林俊杰" in lrc):
        lrc=lrc.split("\n")
        start = 0
        for sentence in lrc:
            if start==1:
                sentence=sentence.split("]")
                if (len(sentence)>=2) and (len(sentence[-1])>=2):
                    lrc_pure.append(sentence[-1])
            if ("演唱：" in sentence) and ("林俊杰" in sentence):
                start=1

    return lrc_pure

def get_pure_lrc(path):
    data=[]
    for ip in os.listdir(path):
        file=path+ip
        ip=ip.split(".")[0]
        with open(file,"r") as f:
            song={}
            lrc_pure=chulitext(f.read())
            if len(lrc_pure)>0:
                song["IP"]=ip
                song["Lrc"]=lrc_pure
                data.append(song)
    return data

def get_lrc_ci(lrc):
    ci=[]
    for sentence in lrc["Lrc"]:
        sentence=list(jieba.cut(sentence))
        sentence_del_stop=[]
        for word in sentence:
            if len(word)>1:
                sentence_del_stop.append(word)
        ci.extend(sentence_del_stop)

    return ci

def get_all_ci(data):
    all_ci=[]
    for lrc in data:
        lrc_ci=get_lrc_ci(lrc)
        all_ci.extend(lrc_ci)
    return  all_ci

def generate_ciyun(cipin):
    cipin_dict={}
    for ci in cipin:
        if ci[0] not in ["活活","四步","两步","这样","一个","it","you","is","and","to","就是","the","be","my","and","your","...","will","on","一天"]:
          cipin_dict[ci[0]]=ci[1]
    wc = WordCloud(
        font_path='msyh.ttf',
        max_words=100,
        background_color='white',
        width=600,
        height=400
    )
    wc.generate_from_frequencies(cipin_dict)

    wc.to_file('LJ.png')

def zhuzhangtu(cipin):
    y=[]
    x_name=[]
    for ci in cipin:
        if ci[0] not in ["活活","四步","两步","这样","一个","it","you","is","and","to","就是","the","be","my","and","your","...","will","on","一天"]:
            y.append(ci[1])
            x_name.append(ci[0])
            if len(y)>=10:
                break
    x=np.arange(len(y))
    pl.figure(1)
    pl.bar(x,y,facecolor = 'red', edgecolor = 'white')
    pl.xticks(x,x_name,fontproperties="SimHei")
    pl.show()


path="LJLyrcFile/"
data=get_pure_lrc(path)
all_ci=get_all_ci(data)
generate_ciyun(Counter(all_ci).most_common())
zhuzhangtu(Counter(all_ci).most_common())




