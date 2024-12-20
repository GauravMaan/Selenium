import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch the browser and navigate to the Facebook login page
driver = webdriver.Safari()
driver.get("https://www.facebook.com/")
time.sleep(3)

# 1. Self
self_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/input")
print("Self Element Tag Name:", self_element.tag_name)

# 2. Child
child_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/child::*")
print("Child Element Tag Name:", child_element.tag_name)

# 3. Parent
parent_element = driver.find_element(By.XPATH, "//*[@class='_6lux']/parent::*")
print("Parent Element Tag Name:", parent_element.tag_name)

# 4. Following
following_element = driver.find_elements(By.XPATH, "//*[@class='_6lux']/following::*")
print("Following Element Tag Name:", len(following_element))

# 5. Preceding
preceding_element = driver.find_elements(By.XPATH, "//*[@class='_6lux']/preceding::*")
print("Preceding Element Tag Name:", len(preceding_element))

# 6. Following-Sibling
following_sibling = driver.find_elements(By.XPATH, "//*[@class='_6lux']/following-sibling::*")
print("Following Sibling Tag Name:", len(following_sibling))

# 7. Preceding-Sibling
preceding_sibling = driver.find_element(By.XPATH, "//*[@class='_6lux']/preceding-sibling::*")
print("Preceding Sibling Tag Name:", preceding_sibling.tag_name)

# 8. Ancestor
ancestor_elements = driver.find_elements(By.XPATH, "//*[@class='_6lux']/ancestor::*")
print("Number of Ancestors:", len(ancestor_elements))
for idx, ancestor in enumerate(ancestor_elements, start=1):
    print(f"Ancestor {idx} - Tag Name: {ancestor.tag_name}, Class Name: {ancestor.get_attribute('class')}")


driver.quit()

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Safari()
# driver.get("https://www.facebook.com/")
# time.sleep(3)
#
# # Locate the element with class '_6lux'
# element = driver.find_element(By.XPATH, "//*[@class='_6lux']")
#
# # Count and list all ancestors
# ancestor_elements = driver.find_elements(By.XPATH, "//*[@class='_6lux']/ancestor::*")
# print("Number of Ancestors:", len(ancestor_elements))
# for idx, ancestor in enumerate(ancestor_elements, start=1):
#     print(f"Ancestor {idx} - Tag Name: {ancestor.tag_name}, Class Name: {ancestor.get_attribute('class')}")
#
# # Count and list all descendants
# descendant_elements = driver.find_elements(By.XPATH, "//*[@class='_6lux']/descendant::*")
# print("\nNumber of Descendants:", len(descendant_elements))
# for idx, descendant in enumerate(descendant_elements, start=1):
#     print(f"Descendant {idx} - Tag Name: {descendant.tag_name}, Class Name: {descendant.get_attribute('class')}")
#
#
# driver.quit()