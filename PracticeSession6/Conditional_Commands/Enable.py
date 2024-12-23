from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.w3schools.com/html/html_forms.asp")
button = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
button.click()
print(button.is_enabled())

driver.quit()