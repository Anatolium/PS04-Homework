from selenium import webdriver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import pprint
import random
import time


def initialize_driver():
    return webdriver.Chrome()


def search_wikipedia(driver, query):
    driver.get("https://ru.wikipedia.org/wiki/" + query.replace(" ", "_"))


def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        pprint.pprint(paragraph.text)
        choice = input("\nEnter – следующий параграф, др.клавиша – назад: ")
        if choice:
            break


def list_internal_links(driver):
    # Переход на связанные страницы
    links = driver.find_elements(By.CSS_SELECTOR, 'div.mw-parser-output > p a')
    random_link = random.choice(links)
    try:
        link = random_link.get_attribute('href')
        # pprint.pprint(link)
        driver.get(link)
    except:
        print(f"------> Ошибка при переходе по ссылке {link}")


def main():
    query = input("------> Введите запрос к Википедии: ")
    driver = initialize_driver()
    search_wikipedia(driver, query)
    while True:
        print("Выберите действие:")
        print("1 – Листать параграфы текущей статьи")
        print("2 – Перейти на одну из связанных страниц")
        print("3 – Вернуться к первоначальному запросу")
        print("Др.клавиша – Завершение")
        choice = input("Ваш выбор: ")

        if choice == '1':
            list_paragraphs(driver)
        elif choice == '2':
            list_internal_links(driver)
        elif choice == '3':
            search_wikipedia(driver, query)
        else:
            break

    driver.quit()

if __name__ == "__main__":
    main()
