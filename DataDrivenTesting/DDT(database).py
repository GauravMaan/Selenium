import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Connect to MySQL database using pymysql
db_connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root1234",
    database="Selenium"
)
cursor = db_connection.cursor()

driver = webdriver.Chrome()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

wait = WebDriverWait(driver, 10)

# Fetch data from MySQL
cursor.execute("SELECT Principle, Rate_of_Interest, Period, Period_Type, Frequency FROM FixedDepositResults")
rows = cursor.fetchall()

for row in rows:
    principle, rate_of_interest, period, period_type, frequency = row
    period_type = period_type.lower()
    print(
        f"Processing data: Principle={principle}, Rate of Interest={rate_of_interest}, Period={period}, Period Type={period_type}, Frequency={frequency}")

    deposit_field = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='principal']")))
    deposit_field.clear()
    deposit_field.send_keys(str(principle))

    time.sleep(2)
    rate_field = driver.find_element(By.ID, "interest")
    rate_field.clear()
    rate_field.send_keys(str(rate_of_interest))

    time.sleep(2)
    tenure_field = driver.find_element(By.ID, "tenure")
    tenure_field.clear()
    tenure_field.send_keys(str(period))

    # Handle the dropdowns for day, month, and year
    tenure_type_dropdown = Select(driver.find_element(By.ID, "tenurePeriod"))
    if "year" in period_type:
        tenure_type_dropdown.select_by_visible_text("year(s)")
    elif "month" in period_type:
        tenure_type_dropdown.select_by_visible_text("month(s)")
    elif "day" in period_type:
        tenure_type_dropdown.select_by_visible_text("day(s)")

    time.sleep(2)
    # Handle the frequency dropdown
    frequency_dropdown = Select(driver.find_element(By.ID, "frequency"))
    frequency_dropdown.select_by_visible_text(frequency)

    time.sleep(2)
    calculate_button = driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img")
    calculate_button.click()

    time.sleep(1)

driver.quit()
cursor.close()
db_connection.close()

