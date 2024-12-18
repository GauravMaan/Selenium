import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Safari()
driver.get("https://demo.guru99.com/test/newtours/")

try:
    register_link = driver.find_element(By.XPATH, "//a[text()='REGISTER']")
    print("REGISTER link located successfully.")
    register_link.click()
    time.sleep(3)
    print("Clicked on the REGISTER link.")
except NoSuchElementException:
    print("REGISTER link not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()