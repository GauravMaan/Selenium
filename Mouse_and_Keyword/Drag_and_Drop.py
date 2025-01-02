import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

oslo=driver.find_element(By.XPATH,"//*[@id='box1']")
wash=driver.find_element(By.XPATH,"//*[@id='box3']")

italy=driver.find_element(By.XPATH,"//*[@id='box101']")
usa=driver.find_element(By.XPATH,"//*[@id='box103']")

act=ActionChains(driver)

act.drag_and_drop(oslo,italy).perform()
act.drag_and_drop(wash,usa).perform()
time.sleep(3)
assert"box1" in italy.get_attribute("innerHTML"),"fail"