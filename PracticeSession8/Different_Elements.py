import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.implicitly_wait(5)
try:
    first_name = driver.find_element(By.XPATH, "//*[@id='name']")
    first_name.send_keys("Gaurav")

    male_radio = driver.find_element(By.XPATH, "//*[@id='gender']")
    female_radio = driver.find_element(By.XPATH, "//*[@id='practiceForm']/div[3]/div/div/div[2]/input")
    male_radio.click()

    # Locate Drop-down Menu
    state_dropdown = driver.find_element(By.XPATH, "//*[@id='state']")
    state_dropdown.click()
    state_name=driver.find_element(By.XPATH,"//*[@id='state']/option[4]")
    state_name.click()

    # Locate Submit Button
    submit_button = driver.find_element(By.XPATH, "//*[@id='practiceForm']/div[11]/input")

    print("Elements located successfully!")

except Exception as e:
    print(f"Error locating element: {e}")


driver.quit()