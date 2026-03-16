# ## Task 2
#
# ### Radio Buttons
#
# Automate interaction with radio buttons `https://demoqa.com/radio-button`
#
# 1. Open the radio button page.
# 2. Print the **title** of the page.
# 3. Locate the **"Yes" radio button**.
# 4. Click the radio button using `click()`.
# 5. Capture and print the **result message** using `.text`.
# 6. Use `get_attribute()` to fetch attributes like:
#    - `class`
#    - `id`
# 7. Print the **current URL**.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(1)

print('Page Title:', driver.title)

yes_radio = driver.find_element(By.ID, 'yesRadio')
yes_radio.click()
sleep(1)

msg = driver.find_element(By.XPATH, '//p[@class="mt-3"]')
print('Result Message:', msg.text)

print('Class Attribute:', yes_radio.get_attribute('class'))
print('ID Attribute:', yes_radio.get_attribute('id'))

print('Current URL:', driver.current_url)

driver.quit()