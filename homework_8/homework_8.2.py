#Task 2
import time
from typing import Callable, Any

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

def perfomance_logger(func: Callable) -> Callable:
    '''
    Это декоратор для вывода логов и времени выполнения функции вместе с самой функцией.

        Args:
            function's arguments

        Returns:
            The wrapped function wrapper.
    '''
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        performance_time = end_time - start_time
        print(f"{PERFORMANCE_LOG_PREFIX} Функция {func.__name__} выполнена за {performance_time:.8f} сек.")
        return result
    return wrapper

@perfomance_logger
def get_sorted_report(revenue_data: list[dict[str, str | float]]):
    """
        Сортирует список по заданному ключу.

        Args:
            revenue_data (list[dict[str, str | float]]): список словарей (данные по выручке жанров).

        Returns:
            revenue_data (list[dict[str, str | float]]): тот список словарей (данные по выручке жанров),
            но уже отсортированный.
        """
    print("Топ категорий по выручке:")
    revenue_data.sorted(key = lambda x : x["total_sales"], reverse = True)
    for i, item in enumerate(revenue_data, start = 1):
        print(f"{i}. {item['category']}: {item.get('total_sales')}")
    return revenue_data

#Tests
first_test = [{"category": "Action", "total_sales": 4311.85},
{"category": "Animation", "total_sales": 4656.30},
{"category": "Children", "total_sales": 3655.55} ]

second_test = [{"category": "Classics", "total_sales": 1200.10},
{"category": "Comedy", "total_sales": 4000.00},
{"category": "Documentary", "total_sales": 4000.00} ]

third_test = [{"category": "Drama", "total_sales": 500.00} ]

print("---ТЕСТ 1---")
get_sorted_report(first_test)
print("---ТЕСТ 2---")
get_sorted_report(second_test)
print("---ТЕСТ 3---")
get_sorted_report(third_test)

