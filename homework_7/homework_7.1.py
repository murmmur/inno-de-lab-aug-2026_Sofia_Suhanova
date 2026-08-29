# Task 1

raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "

# Разбиваем строку по " ; ", получаем список
raw_user_record = raw_user_record.split(" ; ")

#Убираем все пробелы справа и слева, применяем функцию ко всему списку
raw_user_record = list(map(str.strip, raw_user_record))

#Заменяем во втором элементе "_" на пробел
raw_user_record[1] = raw_user_record[1].replace('_', ' ')

#Все элементы списка делаем с заглавной буквы
raw_user_record = [word.title() for word in raw_user_record]

#Добавляем нужный элемент в начало первого элемента
raw_user_record[0] = 'UID-' + raw_user_record[0]

#Приводим третий элемент к верхнему регистру
raw_user_record[2] = raw_user_record[2].upper()

#Приводим последний элемент к нижнему регистру
raw_user_record[3] = raw_user_record[3].lower()

#Снова объединяем наш список в строку
raw_user_record = " | ".join(raw_user_record)

#Итоговый вывод
print(f"Нормализованная запись: {raw_user_record}")

#В условии домашнего задания попросили делать подробные комментарии
