from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Safari()
driver.get("http://www.automationpractice.pl/index.php")
# Step 3: Optionally wait for a few seconds to ensure the page is fully loaded
time.sleep(3)
try:
    # Step 4: Locate the first <h1> element using tag name
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    # Step 5: Print the text content of the <h1> element
    print("Text inside the first <h1> tag:", h1_element.text)
except Exception as e:
    print(f"Error: {e}")
finally:
    # Step 6: Close the browser
    driver.quit()