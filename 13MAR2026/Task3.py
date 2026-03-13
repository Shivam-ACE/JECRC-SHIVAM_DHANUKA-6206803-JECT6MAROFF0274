#TASK-3
# 1. Navigate to https://www.amazon.in/
# 2. Locate the main search bar using its ID with a CSS Selector.
# 3. Locate the Amazon logo (usually an <a> tag with an ID like nav-logo sprites) using a CSS Selector.
# 4. Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
# 5. Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
# 6. Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
# Inspect their common parent and use descendant way and to find all the <a> tags within it.Use find_elements and print the count.


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.amazon.in/")
driver.maximize_window()

sleep(1)

search_bar = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
print("Successfully found search bar ")

logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print("Successfully found the amazon logo")

cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print("Successfully found the cart link")

sign_in = driver.find_element(By.CSS_SELECTOR, "div div a[data-nav-ref='nav_ya_signin']")
print("Successfully found the sign-in link")

categories = driver.find_elements(By.CSS_SELECTOR, "header div div div div div[id='nav-xshop'] a")
print("Total Categories:",len(categories))

driver.quit()