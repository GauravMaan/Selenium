import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.selenium.dev/documentation/")

search_link=driver.find_element(By.PARTIAL_LINK_TEXT,"Web")
search_link.click()
time.sleep(3)
search_link1=driver.find_element(By.LINK_TEXT,"Actions API")
search_link1.click()
time.sleep(2)
driver.quit()
print("Browser closed.")