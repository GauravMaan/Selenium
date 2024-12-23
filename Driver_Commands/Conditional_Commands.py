import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
Logo=driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[1]/a/img").is_displayed()
print(Logo)
Radio_male=driver.find_element(By.XPATH,"//*[@id='gender-male']")
Radio_female=driver.find_element(By.XPATH,"//*[@id='gender-female']")
Radio_male.click()
print(Radio_male.is_enabled())
print(Radio_male.is_selected())

print(driver.title)
print(driver.current_url)
time.sleep(2)

driver.quit()
