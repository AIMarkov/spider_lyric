# import csv
# file=open("name.txt","w")
# writer=csv.writer(file)
# a=[{"name":"陈红名","ID":"11234"}]
# writer.writerow(a[0].values())
# file.close()

##判断是否为中文
import jieba
c="中华民族新气象"
if '\u4e00' <= c <= '\u9fff':
    print(c)
print(list(jieba.cut(c)))

from wordcloud import WordCloud
w=WordCloud()
c="python and wordcloud"
w.generate(c)
w.to_file("test.png")

import matplotlib

print(matplotlib.matplotlib_fname())