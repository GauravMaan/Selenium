import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/#google_vignette")

mini=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
maxi=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print(min.location)
act=ActionChains(driver)

act.drag_and_drop_by_offset(mini,100,0).perform()
act.drag_and_drop_by_offset(maxi,-36,0).perform()
time.sleep(3)
