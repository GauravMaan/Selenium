import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("http://www.automationpractice.pl/index.php/")

search=driver.find_elements(By.TAG_NAME,"input")
for i in search:
    name=i.get_attribute("value")
    print(name)
time.sleep(5)