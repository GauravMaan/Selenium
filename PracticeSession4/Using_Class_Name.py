from selenium import webdriver
from selenium.webdriver.common.by import By
# Step 1: Launch the browser
driver = webdriver.Chrome()  # Ensure 'chromedriver' is in your PATH
# Step 2: Navigate to the website
driver.get("http://www.automationpractice.pl/index.php")
# Step 3: Locate the "Sign In" button using its class name
sign_in_button = driver.find_element(By.CLASS_NAME, "login")
# Step 4: Perform a click action on the button
sign_in_button.click()
print("Done")
# Step 5: Close the browser
driver.quit()