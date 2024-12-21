from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
# Locate the link using partial visible text and click on it
contact_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Contact us")
contact_link.click()
print("Done")
# Close the browser
driver.quit()