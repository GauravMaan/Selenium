from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")
heading = driver.find_element(By.XPATH, "//*[@id='main']/h1")
if heading.text == "HTML Forms":
    print("Heading text is correct")
else:
    print("Heading text is incorrect")
driver.quit()