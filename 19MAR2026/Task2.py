# ---
#
# ## Task 2
#
# ### Registration Form
#
# 1. Go to: https://qavbox.github.io/demo/signup/
# 2. Handle every element in that form
# `Note: Give fake names and emails`
# 3. Click on submit button
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()

wait = WebDriverWait(driver, 6)

name = wait.until(EC.presence_of_element_located((By.ID, 'username')))
name.clear()
name.send_keys("ABC")

email = wait.until(EC.presence_of_element_located((By.ID, 'email')))
email.clear()
email.send_keys("a@bc.com")

number = wait.until(EC.presence_of_element_located((By.ID, 'tel')))
number.clear()
number.send_keys("0123456789")

choose_file = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@multiple="multiple"]')))
choose_file.clear()
choose_file.send_keys(r"I:\WEB-TECH CAP\HTML\assets\4.jpg")

gender = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@name="sgender"]')))
select = Select(gender)
select.select_by_value('male')

wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="one"]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="automationtesting"]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[@value="html"]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//option[@value="selenium"]'))).click()

submit = wait.until(EC.presence_of_element_located((By.ID, 'submit')))
submit.click()

print('Form submitted successfully')

driver.quit()