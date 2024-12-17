import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.wikipedia.org")

Search=driver.find_element(By.ID,"searchInput")
Search.send_keys("Selenium Python")
Search.send_keys(Keys.RETURN)
time.sleep(5)

driver.quit()