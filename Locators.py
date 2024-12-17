import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("http://www.automationpractice.pl/index.php")

search_box=driver.find_element(By.ID,"search_query_top")
search_box.send_keys("T-shirt")
search_box.send_keys(Keys.RETURN)
time.sleep(2)


product=driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts")
product.send_keys(Keys.RETURN)
time.sleep(3)
text=driver.find_element(By.PARTIAL_LINK_TEXT,"Women").text
print("first option",text)

driver.quit()
print("Browser closed.")



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# expected_title = "Search - My Store"
#
#
# driver = webdriver.Safari()
#
# try:
#
#     driver.get("http://www.automationpractice.pl/index.php")
#
#
#     search_box = driver.find_element(By.ID, "search_query_top")
#     search_box.send_keys("T-shirt")
#     search_box.send_keys(Keys.RETURN)
#
#
#     WebDriverWait(driver, 10).until(EC.title_contains("Search"))
#     actual_title = driver.title
#
#
#     if expected_title in actual_title:
#         print("Title Test: Pass")
#     else:
#         print(f"Title Test: Fail - Expected '{expected_title}', but got '{actual_title}'")
#
#
#     product = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.LINK_TEXT, "Faded Short Sleeve T-shirts"))
#     )
#     product.click()
#
#
#     WebDriverWait(driver, 10).until(EC.title_contains("Faded Short Sleeve T-shirts"))
#     print("Product Page Navigation: Pass")
#
# except Exception as e:
#     print(f"An error occurred: {e}")
#
# finally:
#     driver.quit()
#     print("Browser closed.")

