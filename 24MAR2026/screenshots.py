import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

folder = os.path.join(os.getcwd(), 'screenshots')
os.makedirs(folder, exist_ok=True)

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(2)

actions = ActionChains(driver)

# driver.save_screenshot(f'{folder}/screenshot.png')

ele = driver.find_element(By.XPATH, '(//div[@class="e2jAjp XexRYe N9tO7e"]/descendant::img)[8]')
actions.scroll_to_element(ele).perform()
sleep(1)
ele.screenshot(f'{folder}/cherry_red.png')

driver.quit()