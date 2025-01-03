import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(4)
windows = driver.window_handles
print("Window Handles:", windows)
for win in windows:
    driver.switch_to.window(win)
    print("Current Window Title:", driver.title)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Management System":
        print("Closing window with title:", driver.title)
        driver.close()
driver.switch_to.window(windows[0])
print("Active Window Title After Closing:", driver.title)
driver.quit()