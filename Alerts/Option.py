# https://the-internet.herokuapp.com/basic_auth
import time
from selenium import webdriver


ops = webdriver.ChromeOptions()
ops.add_argument("jaldi wha se hato")
driver=webdriver.Chrome()
driver.get("https://whatmylocation.com")
time.sleep(4)
driver.quit()