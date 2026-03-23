from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get(r'I:\SeleniumCAP\20MAR2026\playlist.html')
driver.maximize_window()

songs_list = driver.find_element(By.ID, 'songs')

select = Select(songs_list)

lst = [i.text for i in select.options]

if select.is_multiple:
    for i in lst:
        if 'Girl' in i or 'Love' in i:
            print(i)
            select.select_by_visible_text(i)
driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

driver.quit()