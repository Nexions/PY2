# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Pen:
    def __init__(self, color: str, material: str):
        """
        Создание и подготовка к работе объекта "Ручка"
        :param color: Цвет ручки
        :param material: Материал из которого сделана ручка
        Примеры:
        >>> pen = Pen("синяя", "пластиковая")  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет ручки должен быть типа str")
        self.color = color

        if not isinstance(material, str):
            raise TypeError("Материал ручки должен быть типа str")
        self.material = material

    def color_pen(self) -> bool:
        """
        Функция которая проверяет синяя ли ручка
        :return: Является ли ручка "синяя"
        Примеры:
        >>> pen = Pen("синяя", "пластиковая")
        >>> pen.color_pen()
        """
        ...

    def material_pen(self) -> bool:
        """
        Функция которая проверяет пластиковая ли ручка
        :return: Является ли ручка "пластиковая"
        Примеры:
        >>> pen = Pen("синяя", "пластиковая")
        >>> pen.material_pen()
        """
        ...

class Televisor:
    def __init__(self, diagonal: float, chastota_kadrov: float):
        """
        Создание и подготовка к работе объекта "Телевизор"
        :param diagonal: Диагональ экрана
        :param chastota_kadrov: частота кадров
        Примеры:
        >>> televisor = Televisor(42, 75)  # инициализация экземпляра класса
        """
        if not isinstance(diagonal, (int, float)):
            raise TypeError("Диагональ должна быть типом int или float")
        if diagonal < 0:
            raise ValueError("Диагональ экрана должна быть больше нуля")
        self.diagonal = diagonal

        if not isinstance(chastota_kadrov, (int, float)):
            raise TypeError("Частота должна быть типом int или float")
        if chastota_kadrov < 0:
            raise ValueError("Частота кадров должна быть больше нуля")
        self.chastota_kadrov = chastota_kadrov

    def diagonal_TV(self) -> float:
        """
        Функция которая проверяет диагональ экрана
        :return: диагональ экрана
        Примеры:
        >>> televisor = Televisor(42, 75)
        >>> televisor.diagonal_TV()
        """
        ...

    def chastota_kadrov_TV(self) -> float:
        """
        Функция которая проверяет частоту кадров
        :return: частота кадров
        Примеры:
        >>> televisor = Televisor(42, 75)
        >>> televisor.chastota_kadrov_TV()
        """
        ...

class Table:
    def __init__(self, width: float, length: float, color: str):
        """
        Создание и подготовка к работе объекта "Стол"
        :param width: ширина стола
        :param length: длина стола
        :param color: цвет стола
        Примеры:
        >>> table = Table(50, 120, "белый")  # инициализация экземпляра класса
        """
        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть типом int или float")
        if width < 0:
            raise ValueError("Ширина стола должна быть больше нуля")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть типом int или float")
        if length < 0:
            raise ValueError("Длина стола должна быть больше нуля")
        self.length = length

        if not isinstance(color, str):
            raise TypeError("Цвет стола должен быть типом str")
        self.color = color

    def width_table(self) -> float:
        """
        Функция которая определяет ширину стола
        :return: ширина стола
        Примеры:
        >>> table = Table(50, 120, "белый")
        >>> table.width_table()
        """
        ...

    def length_table(self) -> float:
        """
        Функция которая определяет длину стола
        :return: длина стола
        Примеры:
        >>> table = Table(50, 120, "белый")
        >>> table.length_table()
        """
        ...

    def color_table(self) -> str:
        """
        Функция которая определяет цвет стола
        :return: цвет стола
        Примеры:
        >>> table = Table(50, 120, "белый")
        >>> table.color_table()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
