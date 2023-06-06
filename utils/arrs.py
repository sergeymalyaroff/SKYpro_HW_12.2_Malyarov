"""Функции для работы с массивами"""


def get(array, index, default=None):
    if index < 0 or index >= len(array):
        return default

    return array[index]



def my_slice(coll, start=0, end=None):
    """
    Возвращает новый массив, содержащий копию части исходного массива.
    :param coll: исходный список.
    :param start: индекс, по которому начинается извлечение. Если индекс отрицательный,
    start указывает смещение от конца списка. По умолчанию равен нулю.
    :param end: индекс, по которому заканчивается извлечение (не включая элемент с индексом end).
    Если индекс отрицательный, end указывает смещение от конца списка. По умолчанию равен длине исходного списка.
    :return: массив элементов
    """
    length = len(coll)

    if length == 0:
        return []

    normalized_end = length if end is None else end

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]
