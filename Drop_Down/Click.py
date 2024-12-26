# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Safari()
# driver.get("https://testautomationpractice.blogspot.com/")
# drpdwn=Select(driver.find_element(By.ID,"country"))
# op=drpdwn.options
# for i in op:
#     if i.text=="India":
#         i.click()
#         print(i)
#         break
# time.sleep(5)
#
# chk=driver.find_elements(By.XPATH,"//*[@class='form-check-input' and @type='checkbox']")
#
# for i in range(len(chk)):
#     chk[i].click()
# time.sleep(2)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://testautomationpractice.blogspot.com/")
checkbox = driver.find_elements(By.XPATH, "//*[@class ='form-check-input' and @type='checkbox']")
for i in range(4, 7):
    checkbox[1].click()
    if checkbox[i].is_selected():
        print(1)
        checkbox[i].click()
