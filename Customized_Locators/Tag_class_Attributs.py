import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://en-gb.facebook.com/login/")

search_box=driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=email]")
search_box.send_keys("gaurav"+Keys.RETURN)
time.sleep(2)
search_box1=driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]")
search_box1.send_keys("gaurav"+Keys.RETURN)
time.sleep(2)
driver.quit()