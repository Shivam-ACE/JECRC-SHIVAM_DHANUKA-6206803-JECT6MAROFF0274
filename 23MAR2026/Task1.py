# ---
#
# ## Task 1
#
# ### go to your favourite website
#
# 1. navigate to the website
# 2. scroll to a picture
# 3. scroll up 5 times (using for loop)
#
# ---

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.royalchallengers.com/")
driver.maximize_window()
sleep(1)

action = ActionChains(driver)

vk_jersey = driver.find_element(By.XPATH, '//img[@src="https://tg3.s3.ap-south-1.amazonaws.com/revents/puma-mer/158/71434501_1.jpg"]')
action.scroll_to_element(vk_jersey).perform()
sleep(2)

for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(1)

driver.quit()