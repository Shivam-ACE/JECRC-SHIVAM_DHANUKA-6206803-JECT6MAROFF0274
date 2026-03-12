from selenium import webdriver
import time


url = "https://google.com"

for i in ['Chrome', 'Edge']:

    if i == 'Chrome':
        driver = webdriver.Chrome()

    elif i == 'Edge':
        driver = webdriver.Edge()

    driver.get(url)

    print("URL:", url)
    print("Browser:", i)
    print("Title:", driver.title)

    time.sleep(2)
    driver.quit()