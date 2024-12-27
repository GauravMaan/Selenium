from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/checkboxes")
checkbox = driver.find_element(By.XPATH, "//label[text()='Accept Terms and Conditions']/preceding-sibling::input[@type='checkbox']")
if not checkbox.is_selected():
    checkbox.click()

# Close the browser
driver.quit()