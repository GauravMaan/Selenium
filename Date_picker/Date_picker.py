import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

driver.find_element(By.ID, "datepicker").click()
time.sleep(3)

month = "April"
date = "8"
year = "2025"

while True:
    current_month = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[1]").text
    current_year = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/span[2]").text

    if current_month == month and current_year == year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]").click()
        time.sleep(1)

dates = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td")
for day in dates:
    if day.text == date:
        day.click()

time.sleep(5)

driver.quit()
