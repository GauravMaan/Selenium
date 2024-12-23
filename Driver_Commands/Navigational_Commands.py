import time

from selenium import webdriver

driver = webdriver.Safari()
driver.get("https://www.amazon.in")
print(driver.current_url)
time.sleep(4)
driver.forward()
driver.get("https://www.flipkart.com")
driver.back()
time.sleep(4)
driver.quit()
