from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
wait = WebDriverWait(driver, 20, poll_frequency=2)
username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username.send_keys("Admin")

driver.quit()