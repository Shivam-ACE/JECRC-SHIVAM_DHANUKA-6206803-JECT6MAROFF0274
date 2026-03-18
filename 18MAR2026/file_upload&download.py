from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
# driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()

choose_file = driver.find_element(By.ID, 'file-upload')
choose_file.send_keys(r"C:\Users\shiva\Pictures\Screenshots\Screenshot 2026-02-17 223833.png")

submit_button = driver.find_element(By.ID, 'file-submit')
submit_button.click()

# driver.find_element(By.XPATH, '//a[text()="Screenshot 2025-12-24 164603.png"]').click()
# sleep(10)
# print("downloaded")

driver.quit()