# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Safari()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
#
# window=driver.current_window_handle
# print(window)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(4)
window=driver.window_handles
print(window)
for win in window:
    driver.switch_to.window(win)
    print(driver.title)