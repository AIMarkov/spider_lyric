from selenium import webdriver
import time
driver=webdriver.Firefox()
url="http://music.taihe.com/artist/7994?pst=sug"
driver.get(url)
page_list=driver.find_elements_by_css_selector("a.page-navigator-number")
a_link=driver.find_elements_by_css_selector("a.namelink")
print("第一页包含页面：",[a.text for a in page_list])
print("第一页包含歌曲：",[a.text for a in a_link])
page_list[0].click()
time.sleep(10)#要等click之后最好等driver加载完成，否则是不会变的
page_list=driver.find_elements_by_css_selector("a.page-navigator-number")
a_link=driver.find_elements_by_css_selector("a.namelink")
print("第二页包含页面：",[a.text for a in page_list])
print("第二页包含歌曲：",[a.text for a in a_link])
page_list[1].click()
time.sleep(10)#要等click之后最好等driver加载完成，否则是不会变的
page_list=driver.find_elements_by_css_selector("a.page-navigator-number")
a_link=driver.find_elements_by_css_selector("a.namelink")
print("第三页包含页面：",[a.text for a in page_list])
print("第三页包含歌曲：",[a.text for a in a_link])

driver.close()