from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Safari()
driver.get("http://www.deadlinkcity.com")
links = driver.find_elements(By.TAG_NAME, "a")
active_links = 0
dead_links = 0
for link in links:
    url = link.get_attribute("href")
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                active_links += 1
            else:
                dead_links += 1
        except requests.exceptions.RequestException:
            dead_links += 1
driver.quit()
print(f"Active links: {active_links}")
print(f"Dead links: {dead_links}")