#!/usr/bin/env python3

# coding=utf-8
# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from openpyxl import Workbook
import time


print('speed test-demo1')


test_time=int(2)
URL='http://www.speedtest.net' 
chromedriver='C:\Python\Python37-32\chromedriver.exe'
firefoxdriver="C:\Python\Python37-32\geckodriver.exe"

localtime = time.localtime()
localtime = time.strftime("%Y-%m-%d %H:%M:%S",localtime)


wb=Workbook()
sheet = wb.active
sheet['A1'] = 'ping-speed'
sheet['B1'] = 'download-speed'
sheet['C1'] = 'upload-speed'
sheet['D1'] = 'date'

##column.width
sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 15
sheet.column_dimensions['C'].width = 15
sheet.column_dimensions['D'].width = 20

speedlink=webdriver.Firefox(executable_path=firefoxdriver)
#speedlink=webdriver.Chrome(executable_path=chromedriver)
speedlink.maximize_window()
speedlink.get(URL)
sleep(2)

for i in range(test_time):
    speedlink.find_element_by_class_name('js-start-test').click()
    loop=int(0)
    while loop < 50:
        #ping-speed
        ping_v=speedlink.find_element_by_class_name('ping-speed').text
        #download-speed
        ds_v=speedlink.find_element_by_class_name('download-speed').text 
        #upload-speed
        us_v=speedlink.find_element_by_class_name('upload-speed').text
        loop +=1
        sleep(1)
        #print(loop)
    print('--LOOP:'+str(i)+'-------->')
    print('Ping:'+ping_v+' ms')
    print('Download:'+ds_v+' Mbps') 
    print('Upload:'+us_v+' Mbps') 
    print('Launch time:'+localtime)
    sheet.append([float(ping_v), float(ds_v), float(us_v), localtime])
    

wb.save("sample.xlsx")
sleep(1)
speedlink.close()


