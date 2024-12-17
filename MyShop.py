# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Safari()
# driver.get("http://www.automationpractice.pl/index.php")
#
# image = driver.find_elements(By.TAG_NAME, "img")
# print("Number of images:", len(image))
#
# Link = driver.find_elements(By.TAG_NAME, "a")
# print("Number of links:", len(Link))
#
# Menu = driver.find_elements(By.CLASS_NAME, "sf-menu")[0].text
# print("First Menu Item:", Menu)
#
# driver.quit()
# print("Browser closed.")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("http://www.automationpractice.pl/index.php")

image = driver.find_elements(By.TAG_NAME, "img")
print("Number of images:", len(image))

Link = driver.find_elements(By.TAG_NAME, "a")
print("Number of links:", len(Link))

Menu = driver.find_elements(By.CLASS_NAME, "sf-menu")
for item in Menu:
    print("Menu Item:", item.text)

driver.quit()
print("Browser closed.")