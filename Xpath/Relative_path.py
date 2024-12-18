# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Safari()
# driver.get("https://online.btes.co.in/login/index.php")
# try:
#     username = driver.find_element(By.XPATH, "//*[@id='username']")
#     username.send_keys("gaurav@123")
#     time.sleep(2)
#     password = driver.find_element(By.XPATH, "//*[@id='password']")
#     password.send_keys("Gaurav0009@Venom")
#     password.send_keys(Keys.RETURN)
#     time.sleep(3)
# except Exception as e:
#     print(e)

# import time
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
# driver = webdriver.Safari()
# driver.get("https://online.btes.co.in/login/index.php")
#
# try:
#     username = driver.find_element(By.XPATH, "//*[@id='username']")
#     username.send_keys("gaurav@123")
#     time.sleep(2)
#     password = driver.find_element(By.XPATH, "//*[@id='password']")
#     password.send_keys("Gaurav0009@Venom")
#     password.send_keys(Keys.RETURN)
#     time.sleep(3)
#     try:
#         dashboard = driver.find_element(By.XPATH, "//*[contains(text(), 'Dashboard')]")
#         print("Login successful: Dashboard loaded.")
#     except NoSuchElementException:
#         error = driver.find_element(By.XPATH, "//*[contains(@class, 'error')]").text
#         print(f"Login failed: {error}")
#
# except Exception as e:
#     print(e)
# finally:
#     driver.quit()


import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://online.btes.co.in/login/index.php")


username = driver.find_element(By.XPATH, "//*[@id='username']")
username.send_keys("gaurav@123")
time.sleep(3)
password = driver.find_element(By.XPATH, "//*[@id='password']")
password.send_keys("Gaurav0009@Venom")
time.sleep(5)    
password.send_keys(Keys.RETURN)
time.sleep(10)
links = driver.find_element(By.XPATH, "//*[@class='card-img dashboard-card-img']")
links.click()
time.sleep(10)


    
driver.quit()