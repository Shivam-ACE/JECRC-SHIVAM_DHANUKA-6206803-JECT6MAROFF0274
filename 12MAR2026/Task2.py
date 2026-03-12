from selenium import webdriver
import time

for i in ['Chrome', 'Edge']:

    if i == 'Chrome':
        driver = webdriver.Chrome()

    elif i == 'Edge':
        driver = webdriver.Edge()

    driver.get("https://www.google.com")
    time.sleep(2)
    driver.quit()