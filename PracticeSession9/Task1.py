from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
import time

driver = webdriver.Safari()
driver.get("https://www.expedia.com/")
wait = WebDriverWait(driver, 20)

try:
    time.sleep(5)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'd1-btn')]"))).click()

    today = datetime.today()
    day = today.strftime('%d').lstrip('0')
    month_year = today.strftime('%B %Y')

    while True:
        header = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='uitk-new-date-picker-month']"))).text
        if month_year in header:
            break
        driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
    driver.find_element(By.XPATH, f"//button[@data-day='{day}']").click()

    future_date = today + timedelta(days=7)
    day = future_date.strftime('%d').lstrip('0')
    month_year = future_date.strftime('%B %Y')

    while True:
        header = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='uitk-new-date-picker-month']"))).text
        if month_year in header:
            break
        driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
    driver.find_element(By.XPATH, f"//button[@data-day='{day}']").click()

    specific_date = (today.replace(day=1) + timedelta(days=32)).replace(day=15)
    day = specific_date.strftime('%d').lstrip('0')
    month_year = specific_date.strftime('%B %Y')

    while True:
        header = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='uitk-new-date-picker-month']"))).text
        if month_year in header:
            break
        driver.find_element(By.XPATH, "//button[@aria-label='Next']").click()
    driver.find_element(By.XPATH, f"//button[@data-day='{day}']").click()

    selected_date = driver.find_element(By.ID, "d1-btn").get_attribute("value")
    print(f"Selected Date: {selected_date}")

finally:
    driver.quit()