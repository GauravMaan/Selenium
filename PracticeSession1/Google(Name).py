import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.google.co.in")

Search=driver.find_element(By.NAME,"q")
Search.send_keys("Python programming language")
Search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()