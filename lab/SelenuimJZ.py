from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://music.taihe.com/artist/7994?pst=sug")
print(driver.page_source)
#tag_a=driver.find_elements_by_tag_name('a')
Target_a=driver.find_elements_by_css_selector("a.page-navigator-number")#class对应这CSS设置，不用把class写全
print(len(Target_a))
for i,target_a in enumerate(Target_a):
    # print(i,":",type(target_a))
    # print(i,":",target_a.tag_name)
    # print(i,':',target_a.id)
    # print(i,":",target_a.text)
    if target_a.text in ['1','2','3','4','5']:
        target_a.click()
        #print(driver.page_source)
        exit()
        Target_a=driver.find_elements_by_css_selector("a.page-navigator-number")
        for i,target_a in enumerate(Target_a):
            print(i,":",target_a.tag_name)
            print(i,":",target_a.id)
            print(i,":",target_a.text)
        exit()

driver.close()