from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("https://www.w3schools.com/html/html_tables.asp")

try:
    headers = driver.find_elements(By.XPATH, "//table[@id='customers']//th")
    column_headers = [header.text for header in headers]
    print("Column Headers:", column_headers)

    rows = driver.find_elements(By.XPATH, "//table[@id='customers']//tr")
    table_data = []
    for row in rows:
        cells = row.find_elements(By.XPATH, ".//td")
        row_data = [cell.text for cell in cells]
        if row_data:
            table_data.append(row_data)
    print("Table Data:")
    for row in table_data:
        print(row)

    specific_cell = driver.find_element(By.XPATH, "//table[@id='customers']//tr[3]/td[3]").text
    print("Value of row 2, column 3:", specific_cell)

    numeric_column_index = 2
    numeric_sum = 0
    for row in table_data:
        try:
            numeric_sum += float(row[numeric_column_index - 1])
        except ValueError:
            continue
    print("Sum of numeric values in column 2:", numeric_sum)

finally:
    driver.quit()