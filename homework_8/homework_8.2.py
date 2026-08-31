#Task 2
import time
from typing import Callable, Any

PERFOMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

def perfomance_logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        perfomance_time = end_time - start_time
        print(f"{PERFOMANCE_LOG_PREFIX} Функция {func.__name__} выполнена за {perfomance_time:.8f} сек.")
        return result
    return wrapper

@perfomance_logger
def get_sorted_report(revenue_data: list):
    print("Топ категорий по выручке:")
    revenue_data.sort(key = lambda x : x["total_sales"], reverse = True)
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

