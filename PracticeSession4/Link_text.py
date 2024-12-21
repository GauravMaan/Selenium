from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
# Step 3: Optionally wait for the page to load
time.sleep(3)
try:
    # Step 4: Locate the link by its visible text and click on it
    contact_us_link = driver.find_element(By.LINK_TEXT, "Contact us")
    contact_us_link.click()

    # Optional: Print confirmation of navigation
    print("Clicked on the 'Contact Us' link.")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Step 5: Close the browser
    driver.quit()

    