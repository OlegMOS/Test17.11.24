import numpy as np
import pandas as pd

data = {
    'name': ['Ivan', 'Bob', 'Jon', 'Sirius', 'Anna', 'Jakob', 'Susanna', 'Mariya', 'Nikol', 'Anjela'],
    'subject': ['Russian', 'English', 'Deutsch', 'Chemical', 'Mathematics', 'Russian', 'English', 'Deutsch', 'Chemical', 'Mathematics'],
    'mark': [1, 2, 3, 4, 5, 4, 5, 3, 2, 4]
}

df = pd.DataFrame(data)
print(df.head())

print(f'\nСреднее значение: {df.groupby("subject")["mark"].mean()}')
print(f'\nМедианное значение: {df.groupby("subject")["mark"].median()}')

q1 = df[df["subject"] == "Mathematics"]["mark"].quantile(0.25)
q3 = df[df["subject"] == "Mathematics"]["mark"].quantile(0.75)
IQR = q3-q1

print(f'\nQ1: {q1}')
print(f'\nQ3: {q3}')
print(f'\nIQR: {IQR}')

# Вычисление стандартного отклонения
std_deviation = np.std(df[df["subject"] == "Mathematics"]["mark"])

print("\nСтандартное отклонение оценок по математике:", std_deviation)