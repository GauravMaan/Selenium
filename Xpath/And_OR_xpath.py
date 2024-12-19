import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.facebook.com")
time.sleep(3)
email_field = driver.find_element(By.XPATH, "//input[@id='email' and @type='text']")
email_field.send_keys("email@example.com")
time.sleep(3)
password_field = driver.find_element(By.XPATH, "//input[@id='pass' or @name='pass']")
password_field.send_keys("password")
time.sleep(3)
driver.quit()