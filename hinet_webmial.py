#!/usr/bin/env python3

# coding=utf-8
# -*- coding: utf8 -*-

from selenium import webdriver
from time import sleep

USER="1234"
PASSWD='1234'

URL='https://webmail.hinet.net/'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
sleep(1)
#id="idPuser"
driver.find_element_by_id('idPuser').send_keys(USER)
#id="passPuser"
driver.find_element_by_id('passPuser').send_keys(PASSWD)
#id="OKPuser"
driver.find_element_by_id('OKPuser').click()


