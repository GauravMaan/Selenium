# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
# frm1=driver.find_element(By.XPATH,"//*[@id='frm1']")
# driver.switch_to.frame(frm1)
#
# dropdown = driver.find_element(By.XPATH, "//*[@id='course']")
# dropdown.click()
# print(dropdown.text)
# driver.switch_to.default_content()
# time.sleep(3)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.hyrtutorials.com/p/frames-practice.html")

frm1=driver.find_element(By.XPATH,"//*[@id='frm1']")
driver.switch_to.frame(frm1)

dropdown = driver.find_element(By.ID, "course")
dropdown.click()
driver.find_element(By.XPATH, "//option[text()='Java']").click()
driver.switch_to.default_content()
time.sleep(5)
frm2=driver.find_element(By.XPATH,"//*[@id='frm2']")
driver.find_element(By.XPATH, "//*[@id='selectnav1']").click()
time.sleep(3)
driver.quit()