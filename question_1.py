"""
Представлен алгоритм определения четности числа на основе побитового
сравнения & 1. Его минус в том, что он может быть сложнее для понимания.
Алгоритм с остатком от деления легче читается, но на больших числах операция
деления может давать неверный результат.
"""


def is_even(value):
    return value & 1 == 0
