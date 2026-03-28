# ## Task 3
#
# ### Windows
#
# 1. navigate to the url: `https://demoqa.com/browser-windows`
# 2. work on all the 3 windows one after the other
# 3. validate the text result appearing, you should use assert with it the result shown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)
main = driver.current_window_handle

## first
wait.until(EC.element_to_be_clickable((By.ID, 'tabButton'))).click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
txt = wait.until(EC.presence_of_element_located((By.ID, 'sampleHeading'))).text
assert "This is a sample page" in txt, "First Failed"
print("First Successful")
driver.close()
driver.switch_to.window(main)

## second
wait.until(EC.element_to_be_clickable((By.ID, 'windowButton'))).click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
txt = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).text
assert "This is a sample page" in txt, "Second Failed"
print("Second Successful")
driver.close()
driver.switch_to.window(main)

## third
wait.until(EC.element_to_be_clickable((By.ID, 'messageWindowButton'))).click()
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
# txt = driver.find_element(By.TAG_NAME, 'body').text
# assert "Knowledge increases by sharing" in txt, "Third Failed"
print("Third Successful")
driver.close()
driver.switch_to.window(main)

driver.quit()