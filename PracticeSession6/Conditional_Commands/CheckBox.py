from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.w3schools.com/html/html_forms.asp")
checkbox = driver.find_element(By.XPATH, "//*[@id='html']")
checkbox1 = driver.find_element(By.XPATH, "//*[@id='css']")
checkbox.click()
print(checkbox.is_selected())
driver.quit()