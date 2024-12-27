import time
from selenium import webdriver
from selenium.webdriver.common.by import By

expected_title = "You clicked: Ok"
driver = webdriver.Safari()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
first = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
first.click()
alert = driver.switch_to.alert
# alert.dismiss()
alert.accept()
time.sleep(2)
actual_result = driver.find_element(By.ID, "result").text
if actual_result == expected_title:
    print("Test Passed: The actual result matches the expected title.")
else:
    print(f"Test Failed: Expected '{expected_title}', but got '{actual_result}'.")
driver.quit()
