from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")

click1 = driver.find_element(By.XPATH, "//a[@href='#Multiple']")
click1.click()
time.sleep(3)
frame1 = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(frame1)
frame2 = driver.find_element(By.XPATH, "//iframe")
driver.switch_to.frame(frame2)
input_box = driver.find_element(By.XPATH, "//input[@type='text']")
input_box.send_keys("hello")
time.sleep(3)

driver.switch_to.default_content()
driver.quit()