from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
first_url = driver.current_url
driver.back()
driver.forward()
if driver.current_url == first_url:
    print("Forward navigation command works correctly")
else:
    print("Forward navigation command failed")
driver.quit()