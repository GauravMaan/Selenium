from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.example.com")
parent_element = driver.find_element(By.CSS_SELECTOR, ".parent")
child_element = parent_element.find_element(By.XPATH, ".//a[contains(text(), 'Link 2')]")
child_element.click()
driver.quit()