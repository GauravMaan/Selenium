from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Safari()

driver.get("https://testautomationpractice.blogspot.com/")

table = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table')
rows = table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if not cells:
        cells = row.find_elements(By.TAG_NAME, "th")
    data = [cell.text for cell in cells]
    print("\t".join(data))

driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Safari()
#
# driver.get("https://testautomationpractice.blogspot.com/")
#
# Table = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody')
# for i in Table:
#     print(i.text)
#
# driver.quit()