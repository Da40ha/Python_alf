#!/usr/bin/env python3

# coding=utf-8
# -*- coding: utf8 -*-

from selenium import webdriver
from time import sleep

USER="1234"
PASSWD='1234'

URL='https://twmail.askey.com.tw/owa/auth/logon.aspx?'

driver = webdriver.Firefox()
driver.delete_all_cookies()
driver.maximize_window()
driver.get(URL)
sleep(1)
driver.find_element_by_id('username').send_keys(USER)
driver.find_element_by_id('password').send_keys(PASSWD)
driver.find_element_by_class_name('btn').click()


