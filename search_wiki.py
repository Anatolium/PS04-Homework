from selenium import webdriver
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver import Keys
#Библиотека с поиском элементов на сайте
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title
# print("Открыта страница Википедии")
time.sleep(3)

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys("Солнечная система")
time.sleep(3)

search_box.send_keys(Keys.RETURN)
url = browser.find_element(By.LINK_TEXT, "Солнечная система")
time.sleep(3)

url.click()
time.sleep(3)

