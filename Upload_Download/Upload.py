import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.filemail.com/")
wait = WebDriverWait(driver, 10)
fileUpload = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
filePath = '/Users/gauravmaan/Downloads/Assignment-4(Static Tables,Broken links and Date picker).odt'
fileUpload.send_keys(filePath)
time.sleep(10)
driver.quit()