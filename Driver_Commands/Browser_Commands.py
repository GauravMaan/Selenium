import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
Click=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a")
Click.click()
time.sleep(3)
driver.close()
