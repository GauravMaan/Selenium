import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Safari()
driver.get("https://www.google.co.in")

search_box=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("orangehrm login"+Keys.RETURN)
driver.quit()
print("Browser closed.")