# Task1
"""
def decorator(func):
    def wrapper(data_):
        func(data_)
        count = 0
        for element in data_:
            for item in element:
                if item % 3 != 0:
                    count += 1
        print("К-во значений, не кратных 3: ", count)
        return func(data_)

    return wrapper


@decorator
def special_func(data_):
    new_list_ = []
    for element in data_:
        for item in element:
            if item % 3 == 0:
                new_list_.append(item)
            else:
                pass
    return "Cписок с элементами, кратными 3: ", new_list_


list_ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(special_func(list_))
"""

# Task2
import logging  # Импорт модуля для логгирования


def decorator(func):  # Создание функции декоратор
    def wrapper(*args):  # Создание функции обертки
        # Создание нового  дополнительного кода для функции general_
        spis_ = []  # Создание пустого списка и наполнение его аргументами
        for i in args:
            spis_.append(i)
        # Настраиваем логи: вывод в отдельный файл, уровень лога, формат вывода
        logging.basicConfig(filename='mylog.log', level=logging.INFO,
                            format='%(asctime)s %(levelname)s:%(message)s')
        logging.info(f"Func name and args: {func.__name__, spis_}")  # Логируем имя функции и аргументы
        result = func(*args)  # Присвоение переменной функции
        logging.info(f"Result for func {func.__name__}: {result}")  # Логируем значение, которое возвращает функция
        return func(*args)  # Возврат функции general_

    return wrapper  # Возврат функции wrapper


@decorator  # Декоратор функции
def general_(a, b):  # Объявление функции
    return a ** b


print(general_(4, 2))  # Вызов функции
