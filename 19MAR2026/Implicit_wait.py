from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://abc.com/')
driver.maximize_window()

driver.implicitly_wait(1)

ele = driver.find_element(By.XPATH, '(//a[@class="AnchorLink"]/parent::li/descendant::img)[1]')
print(ele.get_attribute('src'))

driver.quit()