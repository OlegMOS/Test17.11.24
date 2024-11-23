import random
from selenium import webdriver
import time
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте

#Если мы работаем с Chrome
browser = webdriver.Chrome()
#browser.get("https://ru.wikipedia.org/wiki/Selenium")
#browser.save_screenshot("selenium.png")
#time.sleep(5)
#browser.refresh()

browser.get("https://ru.wikipedia.org/wiki")
#Проверяем по заголовку, тот ли сайт открылся
assert "Википедия" in browser.title
time.sleep(5)
browser.refresh()

input_search = input('Введите текст для поиска на wikipedia: ')
#Находим окно поиска
search_box = browser.find_element(By.ID, "searchInput")
#Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
search_box.send_keys(input_search)
#Добавляем не только введение текста, но и его отправку
search_box.send_keys(Keys.RETURN)
time.sleep(5)
a = browser.find_element(By.LINK_TEXT, input_search)
#Добавляем клик на элемент
a.click()

print('')
choice_site = int(input ('Выберите вариант продолжения: 1 - листать страницу; 2 - перейти по ссылке, 3 - выйти: '))

def paragraphs_do():

    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    # Для перебора пишем цикл
    for paragraph in paragraphs:
        print(paragraph.text,end="\n\n")
        choice_site_exit = input('Для вывода следующего параграфа нажмите 1 и затем Enter, для выхода из программы - 3: ')

        if choice_site_exit == '3':
            browser.quit()
            break
        if choice_site_exit == '1':
            print('')
            input()
        else: return choice_site


# Запускаем программу. Каждый раз, нажимая на клавишу Enter, мы будем получать последующий параграф (абзац) текста статьи.

if choice_site == 1:
    paragraphs_do()

def hatnotes_do():

    while True:
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            # Чтобы искать атрибут класса
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        # Проверяем, что список hatnotes не пуст
        if hatnotes:
            print(hatnotes,end="\n\n")
            hatnote = random.choice(hatnotes)
            # Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
        else:
            print("Нет элементов с указанным классом")

        choice_site = int(input('Выберите вариант продолжения: 1 - листать страницу; 2 - перейти по ссылке, 3 - выйти: '))
        if choice_site == 1: paragraphs_do()
        if choice_site == 3: break

if choice_site == 2:
    hatnotes_do()

if choice_site == 3:
    browser.quit()
    #Закрываем браузер