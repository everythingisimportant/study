from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.youtube.com/'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="guide"]')))