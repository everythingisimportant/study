from multiprocessing.connection import wait
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')
msg = driver.find_element('xpath', '//*[@id="user-message"]')
msg.send_keys("Hello")
btn = driver.find_element('xpath', '//*[@id="get-input"]/button')
btn.click()
number1 = driver.find_element('xpath', '//*[@id="sum1"]')
number1.send_keys("10")
number2 = driver.find_element('xpath', '//*[@id="sum2"]')
number2.send_keys("15")
btn = driver.find_element('xpath', '//*[@id="gettotal"]/button')
btn.click()
sleep(10) 