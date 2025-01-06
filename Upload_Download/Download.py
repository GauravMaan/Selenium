import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the download directory
download_path = os.path.expanduser("/Users/gauravmaan/Desktop/Selenium/Upload_Download")

# Configure Chrome options
preferences = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options = Options()
chrome_options.add_experimental_option("prefs", preferences)

# Start the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://github.com/GauravMaan/Selenium")

try:
    wait = WebDriverWait(driver, 10)

    # Locate and click the "Code" button using its aria-label
    code_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=':R55ab:']")))
    code_button.click()

    # Wait for the "Download ZIP" link to appear and click it using link text
    download_zip_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Download ZIP")))
    download_zip_button.click()

    print(f"Repository download initiated. Check the folder: {download_path}")

finally:
    # Close the browser
    driver.quit()