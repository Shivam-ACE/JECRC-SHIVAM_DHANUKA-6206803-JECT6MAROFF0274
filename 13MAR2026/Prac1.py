from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.myntra.com/?gad_campaignid=23550099272")
driver.maximize_window()

sleep(1)
ID1 = driver.find_element(By.ID, "desktop-headerMount")
ID2 = driver.find_element(By.ID, "desktop-header-cnt")
ID3 = driver.find_element(By.ID, "headerSaleBannerCtn")
ID4 = driver.find_element(By.ID, "mountRoot")
ID5 = driver.find_element(By.ID, "amnHalfCard")

NAME1 = driver.find_element(By.NAME, "theme-color")
NAME2 = driver.find_element(By.NAME, "viewport")
NAME3 = driver.find_element(By.NAME, "google-signin-client_id")
NAME4 = driver.find_element(By.NAME, "google-signin-cookiepolicy")
NAME5 = driver.find_element(By.NAME, "google-signin-scope")

CLASS_NAME1 = driver.find_elements(By.CLASS_NAME, "desktop-container")
CLASS_NAME2 = driver.find_elements(By.CLASS_NAME, "desktop-backdropStyle")
CLASS_NAME3 = driver.find_elements(By.CLASS_NAME, "desktop-preHeaderLinks")
CLASS_NAME4 = driver.find_elements(By.CLASS_NAME, "desktop-categoryContainer")
CLASS_NAME5 = driver.find_elements(By.CLASS_NAME, "desktop-bound")

TAG_NAME1 = driver.find_elements(By.TAG_NAME, "input")
TAG_NAME2 = driver.find_elements(By.TAG_NAME, "span")
TAG_NAME3 = driver.find_elements(By.TAG_NAME, "div")
TAG_NAME4 = driver.find_elements(By.TAG_NAME, "script")
TAG_NAME5 = driver.find_elements(By.TAG_NAME, "header")

print(len(CLASS_NAME1))
print(len(CLASS_NAME2))
print(len(CLASS_NAME3))
print(len(CLASS_NAME4))
print(len(CLASS_NAME5))

print(len(TAG_NAME1))
print(len(TAG_NAME2))
print(len(TAG_NAME3))
print(len(TAG_NAME4))
print(len(TAG_NAME5))

driver.quit()