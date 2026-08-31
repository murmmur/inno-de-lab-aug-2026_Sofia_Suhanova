#Task1
MAX_RENTAL_BATCH_LIMIT = 150.0

def calculate_rental_batch(quantity: int, rental_rate: float, batch_num: int, batch_name: str, discount: float = 0.0) -> tuple[float, bool]:
    '''
    Эта функция рассчитывает оптовую стоимость аренды фильмов.

    Parameters
    ----------
    quantity (int): Количество
    rental_rate (float): Значение ренты
    batch_num (int): Номер партии
    batch_name (str): Название партии
    discount (float): Скидка (опционально)

    Returns
    -------
    tuple[float, bool]: Возвращает кортеж, который содержит итоговую стоимость аренды,
    а также говорит превышает ли эта сумма заданную константу.
    '''
    final_sum = round(quantity * rental_rate * (1 - discount), 2)
    is_limit_exceeded = final_sum >= MAX_RENTAL_BATCH_LIMIT
    final_data = (final_sum, is_limit_exceeded)
    print(f"Партия {batch_num} ({batch_name}): Сумма {final_data[0]}$. Превышение лимита: {final_data[1]}")
    return final_data

print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

#Academy Dinosaur
#Вызов с позиционными аргументами
calculate_rental_batch(30, 2.99, 1, "Academy Dinosaur")

#Affair Prejudice
#Вызов с именованными аргументами
calculate_rental_batch(quantity = 40, rental_rate = 4.99, batch_num = 2, batch_name = "Affair Prejudice", discount = 0.1)

#Agent Truman
calculate_rental_batch(10, 1.99, 3, "Agent Truman")

#African Egg
calculate_rental_batch(50, 3.50, batch_num = 4, batch_name = "African Egg", discount = 0.2)

#Можно ли оформлять докстринг в таком стиле как я сделала здесь?
#Когда я ставлю тройные кавычки IDE сама предлагает такой стиль,
#но в презентации он был иным.