"""
Когда отсутствуют какие-то дополнительные сведения о входных данных, считаю что
нужно использовать быструю сортировку: она легко читается и достаточно
эффективная. Да, есть худшие случаи выполенения за O(n**2), но в реальности
они будут встречаться редко. Если бы, условно, сортировали какой-то реальный
массив данных, в которых часто встречаются отсортированные отрезки - можно
было бы воспользоваться встроенной .sort() - Timsort, на таких данных она,
скорее всего, была бы быстрее.
"""
from random import randint


def quicksort(data):
    if len(data) < 2:
        return data

    less, same, more = [], [], []
    pivot = data[randint(0, len(data) - 1)]

    for item in data:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            same.append(item)
        else:
            more.append(item)

    return quicksort(less) + same + quicksort(more)
