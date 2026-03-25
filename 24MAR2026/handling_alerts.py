from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
sleep(2)

####### Simple Alert
# driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]').click()
# alert = driver.switch_to.alert
# alert.accept()
# sleep(2)

####### Confrim Alert
# driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]').click()
# alert = driver.switch_to.alert
# # alert.accept()   #-----------to accept
# alert.dismiss()    #-----------to cancel
# sleep(4)

####### Prompt Alert
# driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
# alert = driver.switch_to.alert
# alert.send_keys("Hiiiiiiiiii")
# alert.accept()
# # alert.dismiss()
# sleep(3)

######## switching to alert using waits
wait.until(EC.presence_of_element_located((By.XPATH, '//button[@onclick="jsPrompt()"]'))).click()
alert = wait.until(EC.alert_is_present())
sleep(2)
alert.send_keys("heyy")
alert.accept()
sleep(2)

driver.quit()