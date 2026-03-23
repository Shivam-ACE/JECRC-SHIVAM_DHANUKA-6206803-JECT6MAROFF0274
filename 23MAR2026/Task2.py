# ---
#
# ## Task 2
#
# ### Myntra
#
# 1. Go to: https://myntra.com
# 2. Hover over any category of your choice and choose one
# 3. scroll to the 5th or 6th row choose a product
# 4. (use proper waits )
# ---

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.myntra.com/")
driver.maximize_window()
sleep(1)

wait = WebDriverWait(driver, 10)

action = ActionChains(driver)

men = wait.until(EC.presence_of_element_located((By.XPATH, '(//div[@class="desktop-navLink"])[1]')))
action.move_to_element(men).perform()
sleep(2)

gadgets = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Gadgets"]')))
gadgets.click()

row = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="28300402"]')))
action.scroll_to_element(row).perform()
sleep(5)

driver.quit()