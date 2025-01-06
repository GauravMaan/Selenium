import os
from selenium import webdriver

driver = webdriver.Safari()

driver.get("https://www.google.com/")

screenshot_path = "/HomePage.png"

driver.save_screenshot(screenshot_path)

current = os.getcwd() + "/HomePage.png"
driver.get_screenshot_as_file(current)

print("Screenshot saved at:", screenshot_path)
print("Screenshot saved at:", current)

# Quit the WebDriver
driver.quit()