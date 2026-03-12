# To open Chrome browser
from selenium import webdriver
from time import sleep

# driver = webdriver.Chrome()
# sleep(5)

# driver.get("https://google.com")

# driver = webdriver.Edge()
# sleep(5)

'''driver = webdriver.Chrome()
driver.get("https://google.com")
sleep(2)

driver.maximize_window()
sleep(2)

driver.back()
sleep(2)

driver.forward()
sleep(2)

driver.refresh()
sleep(2)'''

'''opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= opts)

driver.get("https://google.com")
driver.get("https://instagram.com")

driver.back()
driver.refresh()'''

'''opts = webdriver.EdgeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Edge(options= opts)

driver.get("https://google.com")
driver.get("https://instagram.com")

driver.back()
driver.refresh()'''

'''opts = webdriver.FirefoxOptions()
opts.set_reference('detach', True)
driver = webdriver.Firefox(options= opts)

driver.get("https://google.com")
driver.get("https://instagram.com")

driver.back()
driver.refresh()'''

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options= opts)
driver.maximize_window()

driver.get("https://google.com")
driver.get("https://instagram.com")

driver.back()
driver.refresh()

# driver.close()
driver.quit()