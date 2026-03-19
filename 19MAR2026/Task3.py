# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)
driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

search = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="twotabsearchtextbox"]')))
search.send_keys('Shoes')

suggestion = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="left-pane-results-container"]/div[4]')))
suggestion.click()

sort_by = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-action="a-dropdown-button"]')))
sort_by.click()

newest = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@id="s-result-sort-select_4"]')))
newest.click()

free_shipping = wait.until(EC.presence_of_element_located((By.XPATH, '//li[@id="p_n_free_shipping_eligible/205563695031"]//label')))
free_shipping.click()

prod_name = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="a-section a-spacing-small puis-padding-left-micro puis-padding-right-micro"]//h2/span')))
print('Product name:', prod_name.text)

prod_price = wait.until(EC.presence_of_element_located((By.XPATH, '(//span[@class="a-price"]/span[2])[1]')))
print('Product price:', prod_price.text)

driver.quit()