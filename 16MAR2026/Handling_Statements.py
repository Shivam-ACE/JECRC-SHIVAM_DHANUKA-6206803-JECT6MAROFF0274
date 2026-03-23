from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
# driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(2)

# name = driver.find_element(By.ID, "name")
# name.clear()
# name.send_keys("Shivam")
# sleep(1)
# email = driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
# email.clear()
# email.send_keys("Shivam@123")
# sleep(1)
# driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
# print(driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label').text)
#
# # search = driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
# # search.clear()
# # search.send_keys("S25", Keys.ENTER)
# sleep(1)
# search_button = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
# search_button.click()
# sleep(1)

# print(search.get_attribute('value'))

# print(name.get_attribute("placeholder"))
# print(email.get_attribute("value"))

male = driver.find_element(By.ID, 'male')
male.click()
print(male.is_displayed())
print(male.is_enabled())

check = driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input')
check.click()

print(check.is_selected())
monday_checkbox = driver.find_element(By.XPATH, '//input[@id="monday"]/following-sibling::label')
print(monday_checkbox.text)


driver.quit()