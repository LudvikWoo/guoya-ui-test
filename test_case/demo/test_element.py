# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/8/7 17:35
import time

from selenium.webdriver.support.select import Select


def test_text(driver):
    driver.get('http://localhost:63342/ui-test-15/html/basic/demo.html?_ijt=88g6cuc87nm7vpqh6vhkvduj9s')
    time.sleep(2)
    text = driver.find_element_by_xpath('//input[@type="text"]')
    text.clear()
    text.send_keys('果芽软件')
    time.sleep(2)

def test_pwd(driver):
    driver.get('file:///C:/softwareData/PycharmProjects/ui-test-15/html/basic/demo.html')
    time.sleep(2)
    pwd = driver.find_element_by_xpath('//input[@type="password"]')
    pwd.clear()
    pwd.send_keys('aaa123')
    time.sleep(2)

def test_textarea(driver):
    textarea = driver.find_element_by_xpath('//textarea')
    textarea.clear()
    textarea.send_keys('黄河远上白云间，一片孤城万仞山。')
    time.sleep(2)

def test_radio(driver):
    radio=driver.find_element_by_xpath("//input[@type='radio' and @name='sex'][2]")
    radio.click()
    time.sleep(2)

def test_checkbox(driver):
    checkboxes=driver.find_elements_by_xpath('//input[@type="checkbox" and @name="phone"]')
    for checkbox in checkboxes:
        checkbox.click()
        time.sleep(1)
    time.sleep(2)

def test_button(driver):
    button = driver.find_element_by_xpath('//input[@type="button" and @value="确认"]')
    button.click()
    time.sleep(2)

    alert = driver.switch_to_alert()
    alert.accept()
    time.sleep(2)

def test_select(driver):
    select = driver.find_element_by_xpath('//select[@id="course"]')
    s = Select(select)
    s.select_by_index(2)
    time.sleep(2)
    s.select_by_value('basic-test')
    time.sleep(2)
    s.select_by_visible_text('--请选择--')
    time.sleep(2)

def test_link(driver):
    link = driver.find_element_by_xpath('//a[@href="http://www.baidu.com"]')
    link.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)

def test_date(driver):
    # date=driver.find_element_by_xpath('//input[@type="date" and @name="start_date"]')
    # date.clear()
    # date.send_keys('2019-08-09')
    js = "document.getElementsByName('start_date')[0].removeAttribute('readOnly');" \
         "document.getElementsByName('start_date')[0].setAttribute('value','2019-08-09');"
    driver.execute_script(js)
    time.sleep(3)

def test_time(driver):
    t=driver.find_element_by_xpath('//input[@type="time" and @name="start_time"]')
    t.clear()
    t.send_keys('10:30')
    time.sleep(3)