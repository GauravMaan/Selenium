# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# try:
#     driver = webdriver.Safari()
#     driver.get("https://www.google.com")
#     time.sleep(1)
#
#     search_box = driver.find_element(By.NAME, "q")
#     search_box.send_keys("Bebo Technology" + Keys.RETURN)
#     time.sleep(2)
#     first_result = driver.find_element(By.XPATH, "//h3")
#     first_result.click()
#     time.sleep(1)
# finally:
#     driver.quit()
#     print("Browser closed.")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
expected_title = "bebo Technologies | Software Engineering Services | Offshore Outsourcing"

try:
    driver = webdriver.Safari()
    driver.get("https://www.google.com")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("bebo Technologies" + Keys.RETURN)
    time.sleep(2)

    first_result = driver.find_element(By.XPATH, "//h3")
    first_result.click()
    time.sleep(2)
    actual_title = driver.title
    if actual_title == expected_title:
        print("Test Passed: The actual title matches the expected title.")
    else:
        print(f"Test Failed: Expected '{expected_title}', but got '{actual_title}'.")

finally:
    driver.quit()
    print("Browser closed.")