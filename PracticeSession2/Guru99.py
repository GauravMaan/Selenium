from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://demo.guru99.com/test/newtours/")

try:
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='submit' and @value='Submit']")
    print("Submit button located successfully.")
    submit_button.click()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()