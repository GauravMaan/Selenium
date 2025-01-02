# import time
#
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
# frm=driver.find_element("//*[@id='iframeResult']")
# driver.switch_to.frame(frm)
# driver.find_element(By.XPATH,"//*[@id='field1']").clear()
# time.sleep(3)
# text12=driver.find_element(By.XPATH,"//*[@id='field1']")
# text12.send_keys("welcome")
# time.sleep(3)
# button1=driver.find_element(By.XPATH,"/html/body/button")
# act=ActionChains(driver)
# act.double_click(button1).click().perform()
# time.sleep(3)

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
iframe = driver.find_element(By.ID, "iframeResult")
driver.switch_to.frame(iframe)
text_field = driver.find_element(By.ID, "field1")
text_field.clear()
time.sleep(3)
text_field.send_keys("welcome")
time.sleep(3)
button = driver.find_element(By.XPATH, "/html/body/button")
actions = ActionChains(driver)
actions.double_click(button).perform()
time.sleep(3)
driver.quit()