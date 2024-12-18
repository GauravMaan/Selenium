import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://www.wikipedia.org/")
textbox=driver.find_element(By.XPATH,"//input[@id='searchInput']")
textbox.send_keys("Automation Testing")
time.sleep(5)
button=driver.find_element(By.XPATH,"//i[@class='sprite svg-search-icon']")
button.click()
time.sleep(5)
et="Test automation - Wikipedia"
at=driver.title
if et==at:
    print("Pass")
else:
    print("Fail")