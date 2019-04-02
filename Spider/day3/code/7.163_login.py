#coding:utf-8
from selenium import webdriver

url = 'https://mail.163.com/'

driver = webdriver.Chrome()

driver.get(url)

# 最通用的方法
el_iframe = driver.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
print(el_iframe)

driver.switch_to.frame(el_iframe)

driver.find_element_by_name('email').send_keys('m13074125935')
driver.find_element_by_name('password').send_keys('!QAZ2wsx#EDC')
driver.find_element_by_id('dologin').click()
