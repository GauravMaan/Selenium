import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://en-gb.facebook.com/login/")

search=driver.find_element(By.CSS_SELECTOR,"input#email")
search.send_keys("gaurav"+Keys.RETURN)
time.sleep(2)
search1=driver.find_element(By.CSS_SELECTOR,"input#pass")
search.send_keys("gaurav"+Keys.RETURN)
time.sleep(2)
driver.quit()