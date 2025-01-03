import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://japam.in")
driver.implicitly_wait(3)
driver.maximize_window()


logo=driver.find_element(By.XPATH,"//*[@id='slider-template--23070490493210__collection-list']/div/ul/li[4]/div/div[1]/a")
driver.execute_script("arguments[0].scrollIntoView()",logo)
value=driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(10)