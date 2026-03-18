from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

country_dropdown = driver.find_element(By.ID, 'country')
dropdown = Select(country_dropdown)

# dropdown.select_by_value('australia')
# dropdown.select_by_index(3)
dropdown.select_by_visible_text('Japan')
sleep(2)

driver.quit()