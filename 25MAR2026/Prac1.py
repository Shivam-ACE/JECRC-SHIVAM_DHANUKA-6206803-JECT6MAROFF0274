# Complete Flow On Amazon
# Steps:
# Open website
# Verify homepage title & URL
# Search for product → "Headphones"
# Apply filters (Brand,price(upto 500 or above 1000 anything))
# Open a product → switch to new tab
# Verify product details (title, price) using assert
# Add to cart
# Go to cart verify item (using assert with the name used eailer)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# assert "Amazon" in driver.title, "Homepage title mismatch"
assert "amazon.in" in driver.current_url, "URL mismatch"

wait.until(EC.visibility_of_element_located((By.ID, 'twotabsearchtextbox'))).send_keys("Headphones", Keys.ENTER)
wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@id="p_123/214020"]//i'))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//li[@id="p_36/dynamic-picker-0"]//a'))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="aok-relative"])[1]'))).click()

all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])

prod_title = wait.until(EC.presence_of_element_located((By.ID, 'productTitle'))).text
prod_price = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@id="corePriceDisplay_desktop_feature_div"]//span)[6]'))).text

assert prod_title, "Product title missing"
assert prod_price, "Product price missing"

print("Product:", prod_title)
print("Price:", prod_price)

wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-button'))).click()
wait.until(EC.visibility_of_element_located((By.ID, 'nav-cart-count-container'))).click()
cart_product = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="a-truncate-cut"]'))).text
print('Cart product:', cart_product)
assert prod_title[:10] in cart_product, "Item mismatch in cart"
print("Item Verified")

driver.quit()