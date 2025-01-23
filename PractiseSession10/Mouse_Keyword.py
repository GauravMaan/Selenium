from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)
actions = ActionChains(driver)
box = driver.find_element(By.ID, "hot-spot")
actions.context_click(box).perform()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.get("https://selenium08.blogspot.com/2019/11/double-click.html")
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="post-body-3062664932371252844"]/div/button')
actions.double_click(button).perform()
time.sleep(2)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()


driver.get("https://demoqa.com/droppable/")
time.sleep(2)
drag = driver.find_element(By.ID, "draggable")
drop = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(drag, drop).perform()
time.sleep(2)
print(drop.text)

driver.get("https://demoqa.com/text-box")
time.sleep(2)
name_field = driver.find_element(By.ID, "userName")
email_field = driver.find_element(By.ID, "userEmail")
name_field.send_keys("Gaurav Kumar")
time.sleep(1)
name_field.send_keys(Keys.TAB)
time.sleep(1)
email_field.send_keys("gaurav@example.com")
time.sleep(1)
email_field.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)
time.sleep(2)
print("Submitted")

driver.get("https://inderpsingh.blogspot.com/2014/08/demowebapp_24.html")
time.sleep(2)
distance_field1 = driver.find_element(By.XPATH, '//*[@id="distance"]')
distance_field2 = driver.find_element(By.XPATH, '//*[@id="speed"]')
distance_field1.send_keys("12345")
time.sleep(1)
distance_field1.send_keys(Keys.COMMAND + 'a')
time.sleep(1)
distance_field1.send_keys(Keys.COMMAND + 'c')
time.sleep(1)
distance_field2.send_keys(Keys.COMMAND + 'v')
time.sleep(2)
print("Done")
driver.quit()

driver.get("file:///path/to/your/local/html/file.html")
time.sleep(2)
text_field1 = driver.find_element(By.ID, "field1")
text_field2 = driver.find_element(By.ID, "field2")
text_field1.send_keys("Test Text")
time.sleep(1)
text_field1.send_keys(Keys.COMMAND + 'a')
time.sleep(1)
text_field1.send_keys(Keys.COMMAND + 'c')
time.sleep(1)
text_field2.send_keys(Keys.COMMAND + 'v')
time.sleep(2)

driver.get("https://demoqa.com/tool-tips")
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="toolTipButton"]')
actions.move_to_element(button).perform()
time.sleep(2)
tooltip = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@class='tooltip-inner']"))
)
print(tooltip.text)