import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.facebook.com")

try:
    email_input = driver.find_element(By.CSS_SELECTOR, "input#email")
    print("Email or Phone input box located successfully.")
    time.sleep(3)
    email_input.send_keys("example@test.com")
    time.sleep(3)
    print("Email address entered.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()