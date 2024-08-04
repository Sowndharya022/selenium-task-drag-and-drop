# Using Python Selenium Automation and Action Chains visit the URL
# https://jqueryui.com/droppable/
# and do a Drag and Drop operation of the White Rectangular Box into the Yellow Rectangular Box ?


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()

#switch to iframe
iframe=driver.find_element(By.CLASS_NAME,"demo-frame")
driver.switch_to.frame(iframe)

#draggable and droppable
draggable_element = driver.find_element(By.CSS_SELECTOR, "#draggable")
droppable_element = driver.find_element(By.CSS_SELECTOR, "#droppable")
time.sleep(2)

actions = ActionChains(driver)

actions.drag_and_drop(draggable_element,droppable_element).perform()

time.sleep(5)
# Close the browser
driver.quit()
print("page quit")


