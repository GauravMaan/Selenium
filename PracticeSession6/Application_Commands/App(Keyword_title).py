from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.python.org")
keyword = "Python"
if keyword in driver.title:
    print(f"Title contains the keyword: '{keyword}'")
else:
    print(f"The keyword '{keyword}' is not found in the title.")

# Close the browser
driver.quit()