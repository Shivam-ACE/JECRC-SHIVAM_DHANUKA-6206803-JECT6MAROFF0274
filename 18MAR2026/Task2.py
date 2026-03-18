# ---
#
# ## Task 2
#
# ### Registration Form
#
#
# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
sleep(2)

first_name = driver.find_element(By.ID, 'firstName')
first_name.clear()
first_name.send_keys("ABC")

last_name = driver.find_element(By.ID, 'lastName')
last_name.clear()
last_name.send_keys("XYZ")

email = driver.find_element(By.ID, 'userEmail')
email.clear()
email.send_keys("abc@xyz.com")

gender = driver.find_element(By.ID, 'gender-radio-1')
gender.click()

number = driver.find_element(By.ID, 'userNumber')
number.clear()
number.send_keys("9123456789")

sub = driver.find_element(By.ID, 'subjectsInput')
sub.clear()
sub.send_keys("English")
sub.send_keys(Keys.ENTER)

hobby = driver.find_element(By.XPATH, '//label[text()="Music"]')
hobby.click()

choose_pic = driver.find_element(By.ID, 'uploadPicture')
choose_pic.clear()
choose_pic.send_keys(r"I:\WEB-TECH CAP\HTML\assets\4.jpg")

address = driver.find_element(By.ID, 'currentAddress')
address.clear()
address.send_keys("Jaipur")

state = driver.find_element(By.ID, 'react-select-3-input')
state.clear()
state.send_keys("Rajasthan")
state.send_keys(Keys.ENTER)

city = driver.find_element(By.ID, 'react-select-4-input')
city.clear()
city.send_keys("Jaipur")
city.send_keys(Keys.ENTER)
sleep(5)

submit = driver.find_element(By.XPATH, '//button[@id="submit"]')
submit.click()
sleep(2)

print('Form submitted successfully')

driver.quit()