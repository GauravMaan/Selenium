from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")
page_source = driver.page_source
print(page_source)
driver.quit()