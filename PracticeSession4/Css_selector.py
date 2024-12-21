import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
# Locate the button using a CSS Selector (class and ID) and click on it
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
print("Clicked")
# Close the browser
driver.quit()