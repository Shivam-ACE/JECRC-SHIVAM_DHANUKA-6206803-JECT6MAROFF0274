from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
# driver.refresh()
sleep(2)

driver.find_element(By.XPATH, '//span[@role="button"]').click()

search = driver.find_element(By.XPATH, '//form/div/div/input[@title="Search for Products, Brands and More"]')
search.clear()
search.send_keys("mobiles", Keys.ENTER)
sleep(2)

apple = driver.find_element(By.XPATH, '//div[@title="Apple"]/div/descendant::div[1]')
apple.click()
sleep(2)

img = driver.find_element(By.XPATH, '//a/descendant::div/img[1]')
print(img.get_attribute('src'))

driver.quit()