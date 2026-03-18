from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/sunglasses.html")
driver.maximize_window()
sleep(3)

# eye = driver.find_element(By.ID, 'lrd1')
# print(eye.text)
age = driver.find_element(By.XPATH, '//div[@id="suited_for_id"]/div/div/div/label/div')

# assert "EYEGLASSES" in eye.text, 'Didnt Find'
assert age.is_enabled(), 'Cant do that'
print('Success')

driver.quit()