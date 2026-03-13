from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

# opts.add_argument("--headless")

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

sleep(1)
# name = driver.find_element(By.ID, "name")
# phone_no = driver.find_element(By.ID, "phone")
# nav_bar = driver.find_element(By.NAME, "Navbar")
# radio_button = driver.find_elements(By.CLASS_NAME, "form-check-input")
# # print(radio_button)
# print(len(radio_button))
# inp = driver.find_elements(By.TAG_NAME, "input")
# print(len(inp))

animals = driver.find_element(By.CSS_SELECTOR, "select#animals")
test = driver.find_element(By.CSS_SELECTOR, 'a[href*="testautomationpractice"]')
test2 = driver.find_element(By.CSS_SELECTOR, 'a[href^="http://"]')
test3 = driver.find_element(By.CSS_SELECTOR, 'a[href$=".com"]')
#
# print(animals)
# print(test)
# print(test2)
# print(test3)

ele1 = driver.find_element(By.XPATH, '//div[@itemscope="itemscope"] [@itemprop="blogPost"]')
ele2 = driver.find_element(By.XPATH, '//button[@onclick="toggleButton(this)"]')
ele3 = driver.find_element(By.XPATH, '//input[@value="thursday"]')
ele4 = driver.find_element(By.XPATH, '//button[@onclick="myFunction()"]')
ele5 = driver.find_element(By.XPATH, '//input[@placeholder="Start Date"]')

print(ele1)
print(ele2)
print(ele3)
print(ele4)
print(ele5)

driver.quit()
# print(name)
# print('nav bar Found')