#Task 6: calculator
a=float(input("Enter first num: "))
b=float(input("Enter second num: "))
c=input("Choose operator (+, -, *, /): ")

if c=="+":
    print(f"Результат: {a} + {b} = {a + b}")
elif c=="-":
    print(f"Результат: {a} - {b} = {a - b}")
elif c=="*":
    print(f"Результат: {a} * {b} = {a * b}")
elif c == "/":
    print(f"Результат: {a} / {b} = {a / b}")
else:
    print("Выбран некорректный оператор!")