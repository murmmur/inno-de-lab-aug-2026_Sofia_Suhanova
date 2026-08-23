#Taks 5: number guessing
from random import randint as r
a=0
b=r(1,20)
print(b)
print(f"Я загадал число от 1 до 20. У тебя 5 попыток!")
while a<5:
    c=int(input(f"Попытка {a+1}. Введите число: "))
    a+=1
    if c==b:
        print("Ты угадал! Отличная работа.")
        break
    elif c<b:
        print(f"Слишком мало! Осталось попыток: {5-a}")
    elif c>b:
        print(f"Слишком много! Осталось попыток: {5-a}")

if a==5:
    print("Попытки закончились.")