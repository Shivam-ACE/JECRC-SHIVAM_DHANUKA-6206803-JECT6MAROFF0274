from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

sleep(1)

# ele1 = driver.find_element(By.XPATH, '//div[@itemscope="itemscope"] [@itemprop="blogPost"]')
# ele2 = driver.find_element(By.XPATH, '//button[@onclick="toggleButton(this)"]')
# ele3 = driver.find_element(By.XPATH, '//input[@value="thursday"]')
# ele4 = driver.find_element(By.XPATH, '//button[@onclick="myFunction()"]')
# ele5 = driver.find_element(By.XPATH, '//input[@placeholder="Start Date"]')
#
# print(ele1)
# print(ele2)
# print(ele3)
# print(ele4)
# print(ele5)

# ele1 = driver.find_element(By.XPATH, '//button[text()="Copy Text"]')
# ele2 = driver.find_element(By.XPATH, '//p[text()="Drag me to my target"]')
# ele3 = driver.find_element(By.XPATH, '//a[text()="Youtube"]')
#
# print(ele1)
# print(ele2)
# print(ele3)

ele1 = driver.find_element(By.XPATH, '//option[contains(text(), "Yellow")]')
ele2 = driver.find_element(By.XPATH, '//option[contains(text(), "Lion")]')
ele3 = driver.find_element(By.XPATH, '//button[contains(text(), "Point Me")]')

print(ele1)
print(ele2)
print(ele3)

driver.quit()