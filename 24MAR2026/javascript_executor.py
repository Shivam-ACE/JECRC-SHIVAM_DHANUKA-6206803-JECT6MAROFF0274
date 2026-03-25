from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(5)

# driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# sleep(3)
#
# driver.execute_script("window.scrollTo(0,0);")
# sleep(3)
#
# driver.execute_script("window.scrollBy(0,500);")
# sleep(3)
#
# driver.execute_script("window.scrollBy(0,-200);")
# sleep(3)

ele = driver.find_element(By.XPATH, '(//div[text()="Join Pinterest"])[3]')
driver.execute_script('arguments[0].scrollIntoView();', ele)
sleep(3)

driver.execute_script('arguments[0].click();', ele)
sleep(3)

driver.quit()