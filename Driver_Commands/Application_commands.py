import time

from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)
print(driver.current_url)
time.sleep(2)

driver.quit()
