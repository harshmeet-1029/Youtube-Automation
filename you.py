from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time
import datetime
import subprocess
#link=str(input("Enter the link here")
while True:
    driver = Firefox()# browser
    driver.get('https://www.youtube.com./watch?v=EtiPbWzUY9o')#link
    #search_box = driver.find_element_by_class_name("style-scope ytd-watch-flexy")#
    #search_box.send_keys(Keys.RETURN)
    #------------------------------------------------------------------------------------------------------------|
    print("144p")                                                                                               #|
    try:                                                                                                        #|
        driver.find_element_by_css_selector('button.ytp-button.ytp-settings-button').click()                    #|
        driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()                               #|
        time.sleep(1)   # you can adjust this time                                                               |
        quality = driver.find_element_by_xpath("//span[contains(string(),'144p')]")                             #|   Quality
        print("Element is visible? " + str(quality.is_displayed()))                                             #|
        quality.click()                                                                                         #|
    except:
        try:                                                                                                     #|
            driver.find_element_by_css_selector('style-scope ytd-mealbar-promo-renderer style-text size-default').click()  #|
        except:
            try:
                driver.find_element_by_css_selector('style-scope ytd-button-renderer style-text size-default').click()
            except:
                try:
                    driver.find_element_by_css_selector('yt-simple-endpoint style-scope ytd-button-renderer').click()
                except:
                    pass

        driver.find_element_by_css_selector('button.ytp-button.ytp-settings-button').click()                    #|
        driver.find_element_by_xpath("//div[contains(text(),'Quality')]").click()                               #|
        time.sleep(2)   # you can adjust this time                                                               |
        quality = driver.find_element_by_xpath("//span[contains(string(),'144p')]")                             #|   Quality
        print("Element is visible? " + str(quality.is_displayed()))                                             #|
        quality.click()                                                                                         #|
                                                                                                                #|
    #------------------------------------------------------------------------------------------------------------|
    Xpath= driver.find_element_by_xpath('//div[@id="player-container-inner"]')
    Xpath.click()
    #-----------------------------------------------------------------------------------------|
    print("ad")                                                                              #|
    try:                                                                                     #|
        ad = driver.find_element_by_class_name('ytp-ad-skip-button-container')               #|
        if (ad.is_displayed())=="True":                                                      #|  AD
            ad.click()                                                                       #|
    except:                                                                                  #|
        pass                                                                                 #|
    #-----------------------------------------------------------------------------------------|
    duration = driver.find_element_by_class_name('ytp-time-duration').text                   #|
    _time = time.strptime(duration, '%M:%S')                                                 #|  TIME
    seconds = datetime.timedelta(minutes=_time.tm_min,seconds=_time.tm_sec).total_seconds()  #|
    time.sleep(seconds/2)                                                                    #|
    #-----------------------------------------------------------------------------------------|
    driver.close()
    #-----------------------------------------------------------------------------------------|
    subprocess.run(["./run.sh"])                                                             #| Bash
    #-----------------------------------------------------------------------------------------|
