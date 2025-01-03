from selenium import webdriver
driver=webdriver.Safari()
driver.get("https://www.google.com/")
cookies=driver.get_cookies()
print(cookies)
driver.quit()
