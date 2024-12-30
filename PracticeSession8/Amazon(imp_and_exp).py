from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.amazon.com/")

try:
    # Perform a search query
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptops")
    search_box.send_keys(Keys.RETURN)

    # Explicit wait for search results to load
    wait = WebDriverWait(driver, 15)
    search_results = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@data-component-type, 's-search-result')]"))
    )
    print(f"Number of search results found: {len(search_results)}")

    # Wait for product recommendations on the home page (if we navigate back to the home page)
    driver.get("https://www.amazon.com/")  # Navigate back to home page
    recommendations = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.a-carousel-card"))
    )
    print(f"Number of product recommendations found: {len(recommendations)}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()