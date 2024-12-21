import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Step 1: Launch the browser
driver = webdriver.Chrome()  # Ensure 'chromedriver' is in your PATH
# Step 2: Navigate to the website
driver.get("http://www.automationpractice.pl/index.php")
# Step 3: Locate the search bar using its ID
search_bar = driver.find_element(By.ID, "search_query_top")  # The ID of the search bar
# Step 4: Enter the term "T-shirt/AnyThing you like" and submit the search
search_bar.send_keys("T-shirt")  # Enter text into the search bar
search_bar.send_keys(Keys.RETURN)   # Press Enter to submit the search
time.sleep(2)
print("Item is found")
# Step 6: Close the browser
driver.quit()