# -*- coding:utf-8 -*-
# Author : 小吴老师
# Data ：2019/7/31 15:15

def test_baidu(base_ui):
    base_ui.get('http://www.baidu.com')
    assert '百度' in base_ui.driver.page_source
