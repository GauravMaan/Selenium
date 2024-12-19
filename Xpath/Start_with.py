import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.facebook.com")
time.sleep(3)
email_field = driver.find_element(By.XPATH, "//input[starts-with(@id,'email')]")
email_field.send_keys("email@example.com")
time.sleep(2)
password_field = driver.find_element(By.XPATH, "//input[starts-with(@id,'pass')]")
password_field.send_keys("password")
time.sleep(2)
driver.quit()