from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
sleep(3)

############## Single iframe
# iframe = driver.find_element(By.XPATH, '//iframe[@name="SingleFrame"]')
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("123")
# sleep(5)


######### Nested iframe
driver.find_element(By.XPATH, '(//a[@class="analystic"])[2]').click()
sleep(1)
nested_iframe = driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)
sleep(1)
inner_iframe = driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)
sleep(1)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys("1234")
sleep(5)

driver.switch_to.parent_frame()
driver.switch_to.default_content()

driver.quit()