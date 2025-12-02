class StackEmptyError(IndexError):
    """Попытка взять элемент из пустого стека"""


class QueueEmptyError(IndexError):
    """Попытка взять элемент из пустой очереди"""


class NonIntegerArgumentError(TypeError):
    """
    Аргумент должен быть целым числом
    """


class NegativeArgumentError(ValueError):
    """
    Аргумент не может быть отрицательным
    """


class NonNumericElementError(TypeError):
    """
    Аргумент должен быть числом
    """


class InvalidParameterError(ValueError):
    """
    Неверное значение параметра функции
    """