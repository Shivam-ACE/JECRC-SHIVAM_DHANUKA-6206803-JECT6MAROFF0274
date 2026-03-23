from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.maximize_window()
# sleep(4)
#
# action = ActionChains(driver)
#
# origin_ele = driver.find_element(By.ID, 'column-a')
# target_ele = driver.find_element(By.ID, 'column-b')
#
# action.drag_and_drop(origin_ele, target_ele).perform()
# sleep(2)

############# Mouse Hover
# driver = webdriver.Chrome()
# driver.get("https://supertails.com/")
# driver.maximize_window()
# actions = ActionChains(driver)

# doggo = driver.find_element(By.XPATH, '(//span[contains(text(), "Dogs")])[1]')
# actions.move_to_element(doggo).perform()
# sleep(2)

# catto = driver.find_element(By.XPATH, '//div[@data-ganame="Breed 5"]')
# actions.scroll_to_element(catto).perform()
# sleep(5)
#
# actions.scroll_by_amount(0,-1500).perform()
# sleep(5)

########### Keyboard actions

# actions.send_keys(Keys.PAGE_DOWN).perform()
# sleep(2)
# actions.send_keys(Keys.PAGE_UP).perform()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(2)
# actions.key_up(Keys.CONTROL).perform()
# sleep(2)

############ Copying and pasting for address fields
# driver = webdriver.Chrome()
# driver.get(r"I:\SeleniumCAP\23MAR2026\address_fields.html")
# driver.maximize_window()
# sleep(2)
#
# action = ActionChains(driver)
#
# present = driver.find_element(By.ID, 'presentAddress')
# permanent = driver.find_element(By.ID, 'permanentAddress')

# present.send_keys("JECRC, Jaipur, RAJ.")
# sleep(2)
# present.click()
# action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# sleep(2)
# action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# sleep(2)
#
# permanent.click()
# action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# sleep(2)

# present.send_keys("JECRC, Jaipur, RAJ.")
# sleep(2)
# present.click()
# action.key_down(Keys.CONTROL).send_keys("a").send_keys("c").perform()
# sleep(2)
# permanent.click()
# action.send_keys("v").key_up(Keys.CONTROL).perform()
# sleep(2)
#
# driver.quit()

################ password visibility
driver = webdriver.Chrome()
driver.get(r"I:\SeleniumCAP\23MAR2026\index1.html")
driver.maximize_window()
sleep(2)

action = ActionChains(driver)

driver.find_element(By.ID, "password").send_keys("nik")
sleep(2)
show_pwd = driver.find_element(By.ID, "eyeBtn")
action.click_and_hold(show_pwd).perform()
sleep(4)
action.release().perform()
sleep(5)

driver.quit()