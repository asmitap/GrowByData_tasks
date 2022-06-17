#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
import pandas as pd
import time 
import warnings
warnings.simplefilter(action='ignore', category=Warning)

def html_dump_file(driver, ur):
    f = open(f'./webpage{ur+1}.html', "w",encoding='utf-8')
    h = driver.page_source #obtain page source
    f.write(h)
    f.close()
    
def full_page_screenshots(ur, driver, viewport_height):
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'), S('Height'))
    driver.find_element_by_tag_name('body').screenshot(f"{ur+1}.jpeg")
    driver.set_window_size(S('Width'), viewport_height)
    #time.sleep()
    
def part_part_screenshots(ur, driver):
    viewport_height = driver.execute_script("return window.innerHeight")
    viewport_height -= 80  # -> to obtain full data screenshot
    height = driver.execute_script("return document.body.scrollHeight")
    i = 1  # -> for file name
    y = 0  # -> for equating height left to scroll
    while y < height:
        driver.get_screenshot_as_file("{u}_v{i}.jpeg".format(u=ur+1,i=i))
        name="1_v" + str(i) + ".jpeg"
        driver.get_screenshot_as_file('./name')
        driver.execute_script(f"window.scrollBy(0,{viewport_height})")
        y += viewport_height
        i += 1
    full_page_screenshots(ur, driver, viewport_height)
    
def convert_to_csv(final_dataframe):
    final_dataframe.to_csv("task_2_final.csv",index=False)
    

def main():
    options = webdriver.ChromeOptions()
    options.headless = True # use headless mode screen shots for full page
    driver = webdriver.Chrome(executable_path="E:\growbydata\Growbydata\Task2\chromedriver.exe", options = options)
    dff = pd.read_csv('url.csv')
    urls = dff.values.tolist()
    urls = [item for items in urls for item in items]
    #print(urls)
    final_dataframe = pd.DataFrame()
    link_number = 1
    for ur in range(len(urls)):
        #print(ur)
        driver.get(urls[ur])
        html_dump_file(driver, ur)        # dump file
        #full_page_screenshots(ur, driver) # for full page screenshot
        
        part_part_screenshots(ur, driver) # for part part screen shot
        # for data fetch
        elements = driver.find_elements_by_xpath("//h3/parent::a/ancestor::div[@data-hveid and @data-ved and @class='g tF2Cxc'] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/parent::div[contains(@class,'g')][not(./ancestor::ul)]/parent::div[not(@id) or @id='rso']/div[contains(@class,'g')][not(./ancestor::ul)][not(@data-md)][not(descendant::table)][not(./g-card)][not(parent::div[contains(@class,'V3FYCf')])] | //h3//parent::a/ancestor::div[@data-hveid and @data-ved]/ancestor::div[@class='g']/parent::div[@data-hveid]//div[@data-hveid and @data-ved][not(./ancestor::ul)][not(parent::div[contains(@class,'g ')])] | //h3/parent::a/ancestor::div[contains(@class,'ZINbbc') and contains(@class,'uUPGi')]/parent::div | //a[contains(@href,'youtube')][./h3][not(ancestor::div[contains(@style,'display:none')])]/ancestor::div[not(@*)][parent::div[contains(@class,'g')]]")
        name = []
        link = []
        content = []
        for elem in elements:
            names = elem.find_elements_by_class_name("LC20lb")

            for nam in names:
                name.append(nam.text)

            links= elem.find_elements_by_class_name("TbwUpd.NJjxre")
            for lin in links:
                link.append(lin.text)

            contents = elem.find_elements_by_class_name("VwiC3b")
            for cont in contents:
                content.append(cont.text[0:100])    

        #print(link)
        s1 = pd.Series(name)
        s2 = pd.Series(link)
        s3 = pd.Series(content)
        #print(s3)
        df = pd.concat([s1, s2, s3], axis=1)
        df.columns = ['name', 'link', 'content']
        #print(df)

        indexx = []
        field = []
        value = []
        j=1
        for index,content in df.iterrows():
            for i in range(len(content)):
                indexx.append(f" {link_number}.{j}.{i+1}")
            j=j+1
        j=0        
        for index,content in df.iterrows():
            for i in range(len(content)):
                field.append(content.index[i])
                value.append(content[i])
                j = j+1
        
        link_number = link_number + 1
        # series
        s1 = pd.Series(indexx) 
        s2 = pd.Series(field)
        s3 = pd.Series(value)
        final_df =pd.concat([s1, s2, s3], axis=1)
        final_df.columns = ['index','field','value']
        final_df = final_df.sort_values(by=['field','index'])
        final_dataframe = pd.concat([final_dataframe, final_df])
    #print(final_dataframe)
    convert_to_csv(final_dataframe)

if __name__=="__main__":
    main()


# In[ ]:




