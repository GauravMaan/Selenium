from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.back()
driver.quit()