import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
time.sleep(3)

# 1. Child
child_element = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/child::td[1]/a")
print("Child Element Text:", child_element.text, "| Length:", len(child_element.text))

# 2. Parent
parent_element = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td[1]/a/parent::td")
print("Parent Element Text:", parent_element.text, "| Length:", len(parent_element.text))

# 3. Following
following_element = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td[1]/a/following::td[1]")
print("Following Element Text:", following_element.text, "| Length:", len(following_element.text))

# 4. Preceding
preceding_element = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[2]/td[2]/preceding::td[1]")
print("Preceding Element Text:", preceding_element.text, "| Length:", len(preceding_element.text))

# 5. Following-Sibling
following_sibling = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td[1]/following-sibling::td[1]")
print("Following Sibling Text:", following_sibling.text, "| Length:", len(following_sibling.text))

# 6. Preceding-Sibling
preceding_sibling = driver.find_element(By.XPATH, "//table[@class='dataTable']/tbody/tr[1]/td[2]/preceding-sibling::td[1]/a")
print("Preceding Sibling Text:", preceding_sibling.text, "| Length:", len(preceding_sibling.text))


#7. Ancestor
ancestor_dada=driver.find_element(By.XPATH,"//table[@class='dataTable']/tbody/tr[1]/td[1]/a/ancestor::tr")
print(ancestor_dada.text)
driver.quit()