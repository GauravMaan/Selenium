from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("WebDriver")
driver.get("https://www.google.com/")
driver.quit()