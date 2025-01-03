import time

from selenium import webdriver


driver=webdriver.Safari()
driver.get("https://tailwindcss.com")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,3000)","")
value=driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(5)