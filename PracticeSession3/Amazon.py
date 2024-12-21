# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch a browser (Chrome in this case)
driver = webdriver.Safari()  # Ensure you have 'safari driver' installed and added to PATH.

# Step 2: Navigate to https://www.amazon.com
driver.get("https://www.amazon.com")

# Step 3: Verify the title of the page
expected_title = "Amazon.com. Spend less. Smile more."
actual_title = driver.title

if actual_title == expected_title:
    print("Title verification passed.")
else:
    print(f"Title verification failed. Expected: {expected_title}, but got: {actual_title}")

# Step 4: Close the browser
driver.quit()