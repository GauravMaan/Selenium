from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")
driver.maximize_window()
window_size = driver.get_window_size()

print(f"Window size: {window_size}")
driver.quit()