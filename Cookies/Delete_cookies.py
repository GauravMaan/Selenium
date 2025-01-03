from selenium import webdriver
driver = webdriver.Safari()
driver.get("https://www.google.com/")
driver.delete_all_cookies()
driver.quit()