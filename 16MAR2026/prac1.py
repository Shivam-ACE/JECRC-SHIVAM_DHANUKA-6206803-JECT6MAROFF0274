from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(2)

# genders = driver.find_elements(By.XPATH, '//input[@name="gender"]')
# for gender in genders:
#     sleep(1)
#     gender.click()

days = driver.find_elements(By.XPATH, '//div/div/input[@type="checkbox"]')
for day in days:
    # sleep(1)
    day.click()
    print((day.get_attribute('value')).capitalize())

days[:] = days[::-1]
for day in days:
    # sleep(1)
    day.click()

sleep(1)
driver.quit()