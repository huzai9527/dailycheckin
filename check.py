#/usr/bin/env python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#your chrome driver, i provide win and linux in this project
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)
driver.get("http://ehall.seu.edu.cn/new/index.html")
driver.find_element_by_id("ampHasNoLogin").click()
#replace with your id and password here
driver.find_element_by_id("username").send_keys ("userid")
driver.find_element_by_id("password").send_keys ("password") 
driver.find_element_by_id("xsfw").click()
driver.get('http://ehall.seu.edu.cn/appShow?appId=5821102911870447')
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div[@class='bh-mb-16']/div[1]").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@name='DZ_JSDTCJTW']").send_keys ("36")
driver.find_element_by_id("save").click()
driver.find_element_by_link_text("确认").click()
driver.quit()

