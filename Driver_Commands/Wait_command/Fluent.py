# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Safari()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# wait = WebDriverWait(driver, timeout=30, poll_frequency=.2, ignored_exceptions=[Exception])
# username = driver.find_element(By.NAME, "username")
# username.send_keys("Admin")
# password = driver.find_element(By.NAME, "password")
# password.send_keys("admin123", Keys.RETURN)
#
# print("Login process executed successfully.")
# driver.quit()
# print("Browser closed.")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait = WebDriverWait(driver, timeout=30, poll_frequency=0.2, ignored_exceptions=[Exception])
username = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username.send_keys("Admin")
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys("admin123", Keys.RETURN)
driver.quit()
print("Browser closed.")