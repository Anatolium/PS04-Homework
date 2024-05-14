from selenium import webdriver
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver import Keys
#Библиотека с поиском элементов на сайте
from selenium.webdriver.common.by import By
import time
import random
import pprint

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/Солнечная_система")

# paragraphs = browser.find_elements(By.TAG_NAME, "p")
# for paragraph in paragraphs:
#     pprint.pprint(paragraph.text)
#     input()

hatnotes = []

# Собираем все элементы с тегом "div"
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# pprint.pprint(hatnotes)
hatnote = random.choice(hatnotes)

# Для получения ссылки надо в коде сайта внутри тега "div" найти тег "a" и взять из него часть с атрибутом "href"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)
