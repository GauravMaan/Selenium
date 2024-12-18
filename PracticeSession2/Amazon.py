import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Safari()
driver.get("https://www.amazon.in")

try:
    search_box = driver.find_element(By.XPATH, "//input[contains(@id, 'twotabsearchtextbox') and @type='text']")
    print("Search box located successfully.")
    search_box.send_keys("Laptops")
    time.sleep(3)
    search_box.send_keys(Keys.RETURN)
    print("Search for 'Laptops' initiated.")
    time.sleep(3)
except NoSuchElementException:
    print("Search box not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()