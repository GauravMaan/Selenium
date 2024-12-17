


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Safari()
driver.get("https://www.google.co.in")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("orangehrm login")
search_box.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//h3)[1]")))
first_link = driver.find_element(By.XPATH, "(//h3)[1]")
first_link.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
login_button.click()
time.sleep(5)


driver.quit()
print("Browser closed.")