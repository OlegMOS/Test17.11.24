import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator  # Импортируем GoogleTranslator


# Создаём функцию, которая будет получать информацию
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)  # Запрос отправлен
        response.raise_for_status()  # Проверка на успешность запроса

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    translator = GoogleTranslator(source='en', target='ru')  # Создаём экземпляр GoogleTranslator
    while True:
        # Создаём функцию, чтобы использовать результат функции-словаря
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский язык
        try:
            translated_word = translator.translate(word, target='ru')
            translated_definition = translator.translate(word_definition, target='ru')
        except Exception as e:
            print(f"Ошибка при переводе: {e}")
            continue  # Пропускаем итерацию, если произошла ошибка

        # Начинаем игру
        print(f"Значение слова - {translated_definition}")
        user = input("Что это за слово? ")

        if user.lower() == word.lower():  # Игнорируем регистр
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {translated_word}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n: ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
        break


word_game()