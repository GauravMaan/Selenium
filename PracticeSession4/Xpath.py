from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
element = driver.find_element(By.XPATH, "//a[contains(@href, 'facebook')]")
element.click()
print("Clicked")
driver.quit()