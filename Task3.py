"""
Задача 3-го семинара
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

import logging
from datetime import datetime
import argparse

"""
Создаем файл для логирования
"""
logging.basicConfig(filename='task3.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Dictionary')

def dictionary(text):
    """
    Фyнкция сборки словаря
    """

    text = text.replace(' ', '')
    my_dict = dict()
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

def start (n, t):
    """
    Авторизация пользователя и строки для составления словаря
    """

    name = n
    text = t

    if name != "" and name != "exit":
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} Пользователь {name} запустил программу")
    elif name == "":
        logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Неизвестный пользователь пытался запустить программу")
        raise ValueError("Вы забыли ввести свое имя")
    else:
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} Неизвестный пользователь отказался запускать программу")
        print("Имя пользоваться <exit> - отмена запуска программы")


    if name != "exit":

        if text != "exit" and text != "":
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} Пользователь ввел строку {text}")
            print(dictionary(text))
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} Результат {dictionary(text)}")
        elif text == "":
            logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Передана пустая строка")
            raise ValueError("Передана пустая строка для составления словаря")
        else:
            logger.info(f"{datetime.now().strftime('%H:%M:%S')} Пользователь {name} вышел из программы")
            print("В качестве строки вы передали <exit> - выход из программы")

"""
Получение аргументов из консоли
Справка -> python finish3.py -h
Пример передачи пустой строки -> python Task3.py Alex
Пример, когда пользователь отказался от запуска программы -> python Task3.py exit
Пример, когда пользователь авторизовался, но решил отметить передачу строки -> python Task3.py Alex exit
Пример, рабочей команды -> python Task3.py Alex 'Errors and Exceptions'
"""

parser = argparse.ArgumentParser()
parser.add_argument('n', nargs='?', default="", type=str, help="Имя пользователя")
parser.add_argument('t', nargs='?', default="", type=str, help="Строка для составления словаря")
args = parser.parse_args()

"""
Проверка передаваемых аргументов
"""
if args.n == '':
    logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Неизвестный пользователь пытался запустить программу")
    print("Неизвестный пользователь пытался запустить программу")
else:
    args.n = args.n

if args.t == '':
    logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Передана пустая строка")
    print("Пустая строка")
else:
    args.t = args.t

start(args.n, args.t)
