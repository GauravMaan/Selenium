from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.w3schools.com/html/html_forms.asp")
element = driver.find_element(By.XPATH, "//*[@id='w3-logo']/i")
if element.is_displayed():
    print("Element is displayed")
else:
    print("Element is not displayed")
driver.quit()