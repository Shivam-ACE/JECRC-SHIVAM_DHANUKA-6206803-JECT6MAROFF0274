from gettext import find

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/sunglasses.html")
driver.maximize_window()

sort_dropdown = driver.find_element(By.ID, 'sortByDropdown')
dropdown = Select(sort_dropdown)

dropdown.select_by_value('low_price')
sleep(2)
# prod = driver.find_element(By.XPATH, '//div[@id="152554"]')
# prod = driver.find_element(By.XPATH, '//div[@id="152554"]//div/p')
prod = driver.find_element(By.XPATH, '(//div[@id="card-wrapper-parent"]//div/p)[1]')
print(prod.text)

driver.quit()