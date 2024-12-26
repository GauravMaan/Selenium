from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(5)


username = driver.find_element(By.NAME, "username")
username.send_keys("Admin")
password = driver.find_element(By.NAME, "password")
password.send_keys("admin123", Keys.RETURN)

print("Login process executed successfully.")
driver.quit()
print("Browser closed.")