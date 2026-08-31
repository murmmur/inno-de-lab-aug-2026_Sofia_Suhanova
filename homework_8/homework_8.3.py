from typing import Any

# Константа базового индекса оборачиваемости
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(film_name: str, days_overdue: Any, fine_rate: float) -> tuple[float, float] | None:
    """
    Рассчитывает штраф за просрочку и индекс оборачиваемости.

    Args:
        film_name (str): Название фильма
        days_overdue (Any): Количество дней просрочки (может быть числом,
            строкой, списком)
        fine_rate (float): Штраф за один день просрочки

    Returns:
        tuple[float, float] | None: Кортеж (total_fine, return_index)
        в случае успешного расчёта, иначе None.

    Обрабатываемые ошибки:
        - TypeError: если days_overdue не является числом или строкой.
        - ValueError: если days_overdue не может быть преобразовано в число.
        - ZeroDivisionError: если days_overdue равно нулю.
    """
    try:
        # Преобразуем дни просрочки в число
        numeric_days = float(days_overdue)

        # Рассчитываем итоговый штраф
        total_fine = numeric_days * fine_rate

        # Индекс оборачиваемости
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        # Успешный результат – выводим и возвращаем значения
        print(f"Фильм: '{film_name}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return (total_fine, return_index)

    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_name}': {e}")
        return None

    except ValueError as e:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_name}': {e}")
        return None

    except ZeroDivisionError:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_name}': float division by zero")
        return None

    finally:
        # Всегда выполняется – завершающее сообщение
        print("--- Проверка транзакции возврата завершена ---")


# ---------- ТЕСТЫ ----------
if __name__ == "__main__":
    print("=== ПРОВЕРКА ВОЗВРАТОВ ===")
    calculate_overdue_fine("Matrix", 5, 1.5)
    calculate_overdue_fine("Inception", "пять", 2.0)
    calculate_overdue_fine("Avatar", 0, 2.5)
    calculate_overdue_fine("Interstellar", [3], 3.0)