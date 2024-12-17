# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Safari()
# driver.get("https://demoqa.com/automation-practice-form")
#
# search_box=driver.find_elements(By.TAG_NAME,"input")[0].text
# print(search_box)
# time.sleep(1)
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://demoqa.com/automation-practice-form")
fields = driver.find_elements(By.TAG_NAME, "input")
for i in fields:
    placeholder = i.get_attribute("placeholder")
    if placeholder:
        print(f"Input field placeholder: {placeholder}")
driver.quit()
print("Browser closed.")
