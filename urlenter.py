
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException, TimeoutException
import time
import os
''' This can be used as an template code since the usage of the xpath and css selectors done for my requirement though you can follow through the code to get the idea of
	scrapping using selenium . 
'''
browser= webdriver.Chrome()
username='amit'             #username & password given for login
password='*********'        #you have to fill in these three variables since they are user-defined
url="the url which you need to scrape" 
browser.get(url)
time.sleep(3)
uname=browser.find_element_by_xpath('//*[@id="username"]')
uname.send_keys(username)
time.sleep(2)
passwd=browser.find_element_by_xpath('//*[@id="password"]')
passwd.send_keys(password)
time.sleep(2)
submit= browser.find_element_by_xpath('//*[@id="login-form"]/button/span')
submit.click()
time.sleep(7)

#prints all the servers name which i need to check
f=open("collectinglogs","w+")
logline= browser.find_elements_by_xpath('//*[contains(a,"spl099")]')  # this is a regex used to select lot of servers 
# for getting all the log from the webpage

for log in logline:
    print(log.text)
    f.write(log.text)
    f.write(os.linesep)
    log.click()
    #time.sleep(10)
    try:
        element = WebDriverWait(browser,10000).until(EC.presence_of_element_located((By.XPATH,'//input[@type="text"]')))
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time")
        browser.get(url)
        continue

    try:
        browser.find_element_by_xpath('//input[@type="text"]').send_keys('emc-watch')
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-searchbox")
        continue
    #browser.find_element_by_css_selector('input[type="text"]').send_keys('emc-watch')
    time.sleep(10)
    try:
        browser.find_element_by_xpath('//*[@class="ui-icon ui-icon-arrowthick-1-s"]').click()
        time.sleep(20)
    except(NoSuchElementException ,ElementNotVisibleException, StaleElementReferenceException,TimeoutException):
        print("loading took long time-drilldown")
        continue
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div[6]/h3/a').click()
        time.sleep(20)
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-logname")
        continue
    #browser.find_element_by_xpath('(//input[@type="text"])[3]').send_keys('collecting')
     #-------> this xpath is a way to mark an element in a webpage 
    #time.sleep(10)
    try:
        browser.find_element_by_xpath('//*[@class="ui-icon ui-icon-print"]').click()
        time.sleep(20)
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-logdrilldown")
        continue
    try:
        logs= browser.find_elements_by_xpath('//code')
        for line in logs:
            print(line.text)
            f.write(line.text)
            f.write(os.linesep)
        time.sleep(20)
    except(NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-copycode")
        continue
    try:
        browser.find_element_by_xpath('//*[@id="file-view-close"]/span').click()
        time.sleep(20)
    except (NoSuchElementException,ElementNotVisibleException,StaleElementReferenceException,TimeoutException):
        print("loading took long time-close button")
        continue
    browser.get(url)
    time.sleep(10)

f.close()
browser.find_element_by_xpath('//*[@id="header-logout"]').click()
browser.quit()






  