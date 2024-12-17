import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.selenium.dev")
projects_link = driver.find_elements(By.CLASS_NAME, "nav-link")[3]
projects_link.click()
time.sleep(5)

driver.quit()
print("Browser closed.")