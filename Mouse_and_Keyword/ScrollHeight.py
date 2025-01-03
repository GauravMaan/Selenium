import time

from selenium import webdriver

driver=webdriver.Safari()
driver.get("https://japam.in")
driver.implicitly_wait(3)
driver.maximize_window()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(3)