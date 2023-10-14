# -*- coding: utf-8 -*-
import string

from selenium import webdriver
import urllib, os, pymysql, time

from selenium.webdriver.common.by import By

ISOTIMEFORMAT = '%Y-%m-%d %X'  # Time setup

driver = webdriver.Chrome(executable_path="D:/tools/chromedriver-win64/chromedriver.exe")
count = 0

def save(href,file_path):
    try:
        with open(file_path, 'a+', encoding='utf-8') as file:
            file.write(str(href)+'\n')
        print(f'Saved the string to {file_path} successfully.')
    except Exception as e:
        print(f'Error: {e}')

def find_href(page):
    """
    :param page: 页码
    :return: non
    """
    driver.get('https://www.asos.com/women/dresses/cat/?cid=8799&page=' + page)
    output = driver.find_elements(By.CLASS_NAME, 'productLink_KM4PI')
    global count
    file_path="url"
    for ele in output:
        count += 1
        save(ele.get_attribute('href'), file_path)

for i in range(1, 15):
    find_href(str(i))

print(count)





