from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()


driver.get("https://testautomationpractice.blogspot.com")
time.sleep(3)


calendar_input = driver.find_element(By.ID, "txtDate")
calendar_input.click()
time.sleep(1)

month_dropdown = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[1]")
month_select = Select(month_dropdown)
month_select.select_by_visible_text("April")

year_dropdown = driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[2]")
year_select = Select(year_dropdown)
year_select.select_by_visible_text("2025")

days = driver.find_elements(By.XPATH, "//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")
for day in days:
    if day.text == "8":
        day.click()
        break

time.sleep(3)


driver.quit()