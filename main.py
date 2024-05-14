from search_wiki import webdriver
import time

# Создаём объект browser, который представляет собой экземпляр веб-драйвера для браузера Google Chrome
browser = webdriver.Chrome()

browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
browser.save_screenshot("dom.png")
time.sleep(5)

browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png")
time.sleep(5)
browser.refresh()

browser.quit()
