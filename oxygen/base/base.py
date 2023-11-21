#!/usr/bin/python3
""" Base Functions
Базовые функции """


def round_to_nearest(num: int):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
