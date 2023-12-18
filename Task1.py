"""
Задание 7-го семинара
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
"""
В процессе выполнения программы создается два файла 
task1.log - это файл с логами
test1.txt - это файл с именами
"""

from random import randint, uniform, choice
import logging
from datetime import datetime
import argparse

"""
Создаем файл для логирования
"""
logging.basicConfig(filename='task1.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('ListName')

VOWELS = 'eyuioa'
CONSONANTS = 'qwertsajhgerlwk'
MIN_LEN = 4
MAX_LEN = 7

def fill_names(count, filename):
    logger.info(f"{datetime.now().strftime('%H:%M:%S')} Запуск функции")
    try:
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} Открываем файл для записи имен")
        with (open(filename, 'w', encoding='utf-8') as f):
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} Запускаем цикл создания имен")
            for _ in range(count):
                name_lenght = randint(MIN_LEN, MAX_LEN)
                name = ""
                for i in range(name_lenght):
                    try:
                        name += choice(VOWELS) if i % 2 else choice(CONSONANTS)
                    except NameError as e:
                        logger.error(f"{datetime.now().strftime('%H:%M:%S')} Недостаточное количество значений")
                        raise ValueError("Недостаточное количество значений")
                f.write(name.capitalize() + "\n")
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} Список создан, закрываем цикл создания имен")
    except FileNotFoundError as e:
        logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Не могу открыть файл {e}")
        print("не могу открыть файл")

"""
Получение аргументов из консоли
"""
parser = argparse.ArgumentParser()
parser.add_argument('n', nargs='?', default="10", type=int, help="Количество создаваемых имен (default=10)")
args = parser.parse_args()

"""
Запуск программы из консоли -> python Task1.py 5
Можно с генерировать ошибку, например закоментировать строку 22 - CONSONANTS = 'qwertsajhgerlwk'
после этого запустить программу -> python Task1.py 5
"""

fill_names(args.n, "test1.txt")

"""
Строка для проверки except FileNotFoundError, когда файл для записи не существует
Перед запуском, надо закомментировать рабочий вариант fill_names(args.n, "test2.txt")
"""
#fill_names(args.n, "")

