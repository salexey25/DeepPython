"""
Задание 10-го семинара
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании экземпляра.
У класса должно быть два метода, возвращающие периметр и площадь.
Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
"""
"""
В этой программе хотел сделать cборку try .. except для argparse, но у меня не получилось
отловить ошибку для блока except. Argparse бросает вроде как необычное исключение, а SystemExit,
которое не унаследовано от Exception. Буду думать над этой задачей дальше.
"""


import logging
from datetime import datetime
import argparse

"""
Создаем файл для логирования
"""
logging.basicConfig(filename='task2.log.', encoding='utf-8', level=logging.NOTSET)
logger = logging.getLogger('Rectangle')


class Rectangle():
    """
        Class принимает значение двух сторон и вычисляет площадь и периметр
        """

    logger.warning(f"{datetime.now().strftime('%H:%M:%S')} Был запущен class Rectangle")
    def __init__(self, *args):
        """В args можем получить произвольное количество элементов и для нашего квадрата может прилететь три цифры,
        поэтому мы берем значения по индексам"""
        self.side_1 = args[0]
        if len(args) > 1:
            self.side_2 = args[1]
        else:
            self.side_2 = args[0]

    def square(self):
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} Вычисление площади")
        return self.side_2*self.side_1

    def perimetr(self):
        logger.info(f"{datetime.now().strftime('%H:%M:%S')} Вычисление периметра")
        return (self.side_1+self.side_2) * 2

"""
Запуск программы через консоль -> python Task2.py 6 4
Второй вариант запуска программы через консоль с одним аргументом -> python Task2.py 6
Если запускать программу через консоль без аргументов -> python finish5.py, будет  выведено сообщение,
что требуется хотя бы один аргумент.
"""


parser = argparse.ArgumentParser()
parser.add_argument('l1', nargs='?', default=0, type=int, help="Длина 1-й стороны")
parser.add_argument('l2', nargs='?', default=0, type=int, help="Длина 2-й стороны")
args = parser.parse_args()


if args.l2 == 0:
    logger.info(f"{datetime.now().strftime('%H:%M:%S')} Передано одно значение")
    args.l2 = args.l1

if args.l1 == 0:
    logger.critical(f"{datetime.now().strftime('%H:%M:%S')} Нет значений для вычислений")
    print("Нет значений для вычислений, требуется хотя бы один аргумент. Например <python finish5.py 6>")

a = Rectangle(args.l1,args.l2).square()
b = Rectangle(args.l1,args.l2).perimetr()
print(a,b)