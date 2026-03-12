from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()

# driver = webdriver.Edge()

driver = webdriver.Firefox()
driver.get("https://google.com")
sleep(5)
