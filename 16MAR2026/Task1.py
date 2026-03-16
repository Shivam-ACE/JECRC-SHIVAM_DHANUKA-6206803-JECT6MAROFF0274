# ## Task 1
#
# ### OrangeHRM Login
#
# Automate the login flow in OrangeHRM and verify that the user successfully reaches the dashboard:
#
# 1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
# 2. Get and print the title of the page.
# 3. Locate the username input field and use clear() if needed.
# 4. Enter the username using send_keys().
# 5. Locate the password input field and enter the password using send_keys().
# 6. Submit the login form using either: click() on the Login button, or Keys.ENTER
# 7. After login, print the current URL.
# 8. Check if dashboard is present in that url using `in`
# 9. Print 'successful login'
#
# Test Data:
#
# Username: `Admin`
# Password: `admin123`

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = opts)
driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
sleep(2)

print("Page Title:", driver.title)

username = driver.find_element(By.XPATH, '//input[@name="username"]')
username.clear()
username.send_keys('Admin')
sleep(1)

password = driver.find_element(By.XPATH, '//input[@name="password"]')
password.clear()
password.send_keys('admin123')
sleep(1)

driver.find_element(By.XPATH, '//button').click()
sleep(2)

curr_url = driver.current_url
print("Current URL (After Login):", curr_url)

if 'dashboard' in curr_url:
    print('Successful Login')
else:
    print('Failed Login')

driver.quit()