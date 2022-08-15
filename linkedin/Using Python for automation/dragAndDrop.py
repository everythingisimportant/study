from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element('xpath', '//*[@id="box3"]')
destination = driver.find_element('xpath', '//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()
sleep(5)