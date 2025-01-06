import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.booking.com/")

try:
    links = driver.find_elements(By.TAG_NAME, "a")
    urls = []
    for link in links:
        try:
            href = link.get_attribute("href")
            if href:
                urls.append(href)
        except Exception as e:
            continue

    broken_links = []
    for url in urls:
        try:
            response = requests.head(url, timeout=5)
            if response.status_code != 200:
                broken_links.append((url, response.status_code))
        except requests.RequestException as e:
            broken_links.append((url, str(e)))

    print("Broken Links:")
    for link, error in broken_links:
        print(f"{link} - {error}")

finally:
    driver.quit()