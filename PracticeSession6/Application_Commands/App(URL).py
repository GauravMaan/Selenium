# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get( "https://www.python.org")
# print(driver.current_url)
# driver.quit()

from selenium import webdriver
driver = webdriver.Chrome()
expected_url = "https://www.python.org/"
driver.get(expected_url)
current_url = driver.current_url
if current_url == expected_url:
    print("The URL matches the expected URL.")
else:
    print("The URL does not match the expected URL.")
driver.quit()