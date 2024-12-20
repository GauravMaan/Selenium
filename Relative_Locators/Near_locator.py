from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver=webdriver.Safari()

driver.get("https://automationbookstore.dev")

near_locator = driver.find_element(locate_with(By.TAG_NAME, 'li').near({By.ID: 'pid2'})).text
print(near_locator)
right_locator = driver.find_element(locate_with(By.TAG_NAME, 'li').to_right_of({By.ID: 'pid2'})).text
print(right_locator)
left_locator = driver.find_element(locate_with(By.TAG_NAME, 'h2').to_left_of({By.ID: 'pid2'})).text
print(left_locator)
below_locator = driver.find_element(locate_with(By.TAG_NAME, 'h2').below({By.ID: 'pid2'})).text
print(below_locator)

