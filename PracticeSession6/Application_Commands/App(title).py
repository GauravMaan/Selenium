from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")
page_title = driver.title

print(f"Page title: {page_title}")
driver.quit()