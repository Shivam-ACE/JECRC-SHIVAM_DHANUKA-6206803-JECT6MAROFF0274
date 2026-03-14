from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver1 = webdriver.Chrome()
# driver2 = webdriver.Chrome()
# driver3 = webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
sleep(1)
# driver1.get("https://www.amazon.in/")
# sleep(2)
# driver2.get("https://www.cricbuzz.com/")
# sleep(2)
# driver3.get("https://www.myntra.com/")
# sleep(2)

# ele1 = driver1.find_element(By.XPATH, '//span[text()="All"]/ancestor::div[@id="nav-main"]')
# //div[@id="nav-main"]/descendant::span[text()="All"]

# //span[text()="All"]/parent::a
# //a[@id="nav-hamburger-menu"]/child::span

# ele2 = driver1.find_element(By.XPATH, '//a[text()="Fresh"]/ancestor::li/following-sibling::li[1]')

# driver.find_element(By.LINK_TEXT, "Udemy Courses")
# print('link found')
# driver.find_element(By.PARTIAL_LINK_TEXT, "Udemy")
# print('link found')

# //td[text()="Learn Java"]/following-sibling::td[3]
# //td[text()="Amod"]/ancestor::tbody/descendant::td[3]

# book_name = driver.find_elements(By.XPATH, '//td[text()="300"]/preceding-sibling::td[3]')
# print(book_name)

browser_name = driver.find_elements(By.XPATH, '//tbody[@id="rows"]/descendant::tr/descendant::td[1]')
print(browser_name)