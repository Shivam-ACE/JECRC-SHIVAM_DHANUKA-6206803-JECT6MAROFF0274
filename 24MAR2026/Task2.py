# ## Task 2
#
# ### Alerts
#
# 1. navigate to the url: `https://demoqa.com/alerts`
# 2. work on all the 4 alerts one after the other
# 3. validate the result appearing, eg: for `ok` you should assert with it the result shown
# ---

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
actions = ActionChains(driver)

### First Alert
wait.until(EC.element_to_be_clickable((By.ID, 'alertButton'))).click()
alert = wait.until(EC.alert_is_present())
alert.accept()

### Second
wait.until(EC.element_to_be_clickable((By.ID, 'timerAlertButton'))).click()
alert = wait.until(EC.alert_is_present())
alert.accept()

### Third
wait.until(EC.element_to_be_clickable((By.ID, 'confirmButton'))).click()
alert = wait.until(EC.alert_is_present())
alert.accept()

confirm = wait.until(EC.presence_of_element_located((By.ID, 'confirmResult')))
assert "Ok" in confirm.text, "Confirm alert not handled"

### Fourth
wait.until(EC.element_to_be_clickable((By.ID, 'promtButton'))).click()
alert = wait.until(EC.alert_is_present())
alert.send_keys("XYZ")
alert.accept()

res = wait.until(EC.presence_of_element_located((By.ID, 'promptResult')))
assert "XYZ" in res.text, "Prompt alert not handled"

print("All Four Alerts are Handled")

driver.quit()