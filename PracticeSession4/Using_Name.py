from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Step 1: Launch the browser
driver = webdriver.Chrome()  # Ensure 'chromedriver' is in your PATH
# Step 2: Navigate to the website
driver.get("http://www.automationpractice.pl/index.php")
# Step 3: Locate the search field using the name attribute
search_field = driver.find_element(By.NAME, "search_query")  # Name attribute of the search bar
# Step 4: Perform an action (enter text and press Enter)
search_field.send_keys("T-Shirt")  # Enter text
search_field.send_keys(Keys.RETURN)        # Submit the search by pressing Enter
print("Done")
# Step 5: Close the browser after the task
driver.quit()

