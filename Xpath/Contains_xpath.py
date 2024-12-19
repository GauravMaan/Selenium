import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.facebook.com")
time.sleep(3)
email = driver.find_element(By.XPATH, "//input[contains(@id,'email')]")
email.send_keys("email@example.com")
time.sleep(3)
password = driver.find_element(By.XPATH, "//input[contains(@id,'pass')]")
password.send_keys("password")
time.sleep(3)
driver.quit()