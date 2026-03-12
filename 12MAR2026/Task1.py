from selenium import webdriver
from time import sleep

'''driver = webdriver.Chrome()

sleep(5)
driver.maximize_window()
sleep(5)
driver.get("https://google.com")
sleep(5)
driver.back()
sleep(5)
driver.refresh()
sleep(5)
driver.forward()
sleep(5)'''

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= opts)

driver.get("https://google.com")
sleep(5)

driver.quit()