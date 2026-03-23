from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

cal = driver.find_element(By.ID, 'datepicker').send_keys("03/30/2026", Keys.ENTER)
sleep(2)

month = 'May'
date = '2'

driver.find_element(By.ID, 'txtDate').click()
sleep(1)

select = Select(driver.find_element(By.XPATH, '//select[@data-handler="selectMonth"]'))
select.select_by_visible_text(month)
driver.find_element(By.XPATH, f'//a[text()="{date}"]/parent::td').click()
sleep(1)

driver.quit()