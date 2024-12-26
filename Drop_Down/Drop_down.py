from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()
driver.get("https://testautomationpractice.blogspot.com/")
dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "country"))
)
select = Select(dropdown)
select.select_by_visible_text("United States")
print("Selected by visible text:", select.first_selected_option.text)
select.select_by_value("usa")
print("Selected by value:", select.first_selected_option.text)
options = select.options
if len(options) > 3:
    select.select_by_index(3)
    print("Selected by index:", select.first_selected_option.text)
else:
    print("Index 3 is out of range")

driver.quit()