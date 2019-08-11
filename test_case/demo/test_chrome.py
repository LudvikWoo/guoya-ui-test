# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/8/7 11:56
import time
from selenium import webdriver

def test_baidu(driver):
    driver.get('http://www.baidu.com')
    time.sleep(2)

def test_open():
    driver = webdriver.Chrome('../chrome_driver/chromedriver.exe')
    time.sleep(2)

def test_close():
    driver = webdriver.Chrome('../chrome_driver/chromedriver.exe')
    time.sleep(2)

    driver.quit()

def test_max():
    driver = webdriver.Chrome('../chrome_driver/chromedriver.exe')
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)

def test_get(driver):
    driver.get('http://www.baidu.com')
    time.sleep(2)
    driver.get('http://www.jd.com')
    time.sleep(2)

def test_nav(driver):
    driver.get('http://www.baidu.com')
    time.sleep(2)
    driver.get('http://www.jd.com')
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(2)
    driver.refresh()
    time.sleep(2)