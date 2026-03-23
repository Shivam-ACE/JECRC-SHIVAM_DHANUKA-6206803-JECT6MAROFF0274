from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep



opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome()
driver.get('https://demoqa.com/droppable')
driver.maximize_window()
sleep(3)

wait=WebDriverWait(driver,5)
draggable=wait.until(ec.visibility_of_element_located((By.ID,'draggable')))
droppable=wait.until(ec.visibility_of_element_located((By.ID,'droppable')))

action=ActionChains(driver)
action.drag_and_drop(draggable,droppable).perform()
sleep(3)

validate=wait.until(ec.visibility_of_element_located((By.XPATH,'//div[@id="droppable"]/p')))
assert validate.text=='Dropped!', 'Error'

# new_page=driver.find_element(By.ID,'droppableExample-tab-preventPropogation')
# new_page.click()
# wait=WebDriverWait(driver,5)
# dragbox=wait.until(ec.presence_of_element_located((By.ID,'dragBox')))
# outerbox1=wait.until(ec.presence_of_element_located((By.ID,'notGreedyDropBox')))
# innerbox1=wait.until(ec.presence_of_element_located((By.ID,'notGreedyInnerDropBox')))
#
# action=ActionChains(driver)
# action.drag_and_drop(dragbox,outerbox1).perform()
# action.drag_and_drop(dragbox,innerbox1).perform()
# sleep(4)

driver.quit()