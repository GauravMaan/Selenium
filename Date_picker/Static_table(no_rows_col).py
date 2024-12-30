from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://testautomationpractice.blogspot.com/")
table = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table')
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
column_count = len(rows[0].find_elements(By.TAG_NAME, "th") or rows[0].find_elements(By.TAG_NAME, "td"))
print(row_count)
print(column_count)

driver.quit()