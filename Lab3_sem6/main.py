from mypackage.module1 import find_spring_dates
from mypackage.module2 import count_words_starting_with

# Пример использования для задачи 13
filename_text = "Lab3_sem6/texst.txt"
letter = 'с'
count = count_words_starting_with(filename_text, letter)
print(f"Количество слов, начинающихся с буквы '{letter}': {count}")

# Пример использования для задачи 17
filename_dates = "Lab3_sem6/dates.txt"
spring_dates = find_spring_dates(filename_dates)
print("Весенние даты:")
for date in spring_dates:
    print(date)