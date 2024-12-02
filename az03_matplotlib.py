import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Генерация случайных чисел, распределенных по нормальному распределению
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=6)
plt.xlabel("x ось")
plt.ylabel("y ось")
plt.title("Тестовая гистограма случайного ряда")
plt.show()

def diagram_random(random_array_x, random_array_y):
    plt.scatter(random_array_x, random_array_y)
    plt.xlabel("ось Х")
    plt.ylabel("ось Y")
    plt.title("Тестовая диаграмма рассеяния")
    plt.show()

i = 0
for i in range(0,2):
    i = i + 1
    random_array_X= np.random.rand(5)  # массив из 5 случайных чисел
    random_array_Y= np.random.rand(5)
    diagram_random(random_array_X, random_array_Y)

#Парсинг цен с сайта divan.ru и вывод среднего значения и гистограммы цен

data = pd.read_csv('Price_lights_divan.csv')

# Преобразуем столбец в числовой формат, если в нем есть нечисловые значения
data['Цена, руб.'] = pd.to_numeric(data['Цена, руб.'], errors='coerce')
# Преобразуем в целые числа, игнорируя NaN
prices = data['Цена, руб.'].dropna().astype(int)


print(f'\nСредняя цена на светильники на divan.ru: {int(prices.mean())} руб. с НДС')
plt.hist(prices, bins=10, edgecolor='black')
# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')
# Показать гистограмму
plt.show()