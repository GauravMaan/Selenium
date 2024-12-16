import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Safari()
    time.sleep(1)
    driver.get("https://www.google.com")
    time.sleep(1)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Bebo Technology" + Keys.RETURN)
    time.sleep(2)
    driver.implicitly_wait(5)

finally:
    driver.quit()
    print("Browser closed.")