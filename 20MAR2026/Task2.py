from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get(r'I:\SeleniumCAP\20MAR2026\playlist.html')
driver.maximize_window()

songs = driver.find_elements(By.XPATH, '//optgroup[@label="One Direction"]/option')
# songs_lst = [song.text for song in songs]

all_songs_list = driver.find_element(By.ID, 'songs')

select = Select(all_songs_list)

# for song in songs:
#     song.click()

if  select.is_multiple:
    for song in songs:
        if song in driver.find_elements(By.XPATH, '//optgroup[@label="One Direction"]/option'):
            select.select_by_visible_text(song.text)

driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

print('Songs by One Direction:', [i.text for i in select.all_selected_options])
driver.quit()