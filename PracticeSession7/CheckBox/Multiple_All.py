from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()

driver.quit()