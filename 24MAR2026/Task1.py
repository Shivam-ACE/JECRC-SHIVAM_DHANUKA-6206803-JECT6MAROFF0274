# ## Task 1
#
# ### https://codepen.io/gdw96/pen/jOypoYL
#
# 1. navigate to the above url
# 2. enter username and password
# 3. click on hold on the eye to view password
# 4. click on register
# 5. Use sleep for 5sec then refresh the page
# 6. Validate the word `Registration` using assert
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

iframe = wait.until(EC.presence_of_element_located((By.ID, 'result')))
driver.switch_to.frame(iframe)

username = wait.until(EC.visibility_of_element_located((By.ID ,'username')))
username.clear()
username.send_keys("ABC")
password = wait.until(EC.visibility_of_element_located((By.ID ,'password')))
password.clear()
password.send_keys("ABC@123")

psswd_vis_btn = wait.until(EC.visibility_of_element_located((By.ID, 'showPsswd')))
actions.click_and_hold(psswd_vis_btn).perform()
sleep(4)
actions.release().perform()
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@value="Register"]'))).click()
sleep(5)

driver.refresh()

iframe = wait.until(EC.presence_of_element_located((By.ID, 'result')))
driver.switch_to.frame(iframe)

reg = wait.until(EC.visibility_of_element_located((By.XPATH, '//h1[text()="Registration"]')))
assert "Registration" in reg.text, "Registration text not found"
print("Success")

driver.quit()