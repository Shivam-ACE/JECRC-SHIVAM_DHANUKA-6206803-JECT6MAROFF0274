# ---
#
# ## Task 1
#
# ### abc.com To fetch banner images
#
# 1. Go to abc.com
# 2. Find the banners
# 3. Print the image links
#
# ---

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://abc.com/')
driver.maximize_window()

wait = WebDriverWait(driver, 6)

banners = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="hero-items"]//picture/img')))
for banner in banners:
    print(banner.get_attribute('src'))

driver.quit()