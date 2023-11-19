#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Основной файл
 Файл: oxygen.py
--------------------------------------------------------------------------------
 Описание: Главный файл, содержащий импорты всех библиотек и функций
"""
from oxygen.chemistry.base import calculate_relative_molecular_mass, read_formula


def main():
    formula = input('Введите формулу: ')
    mass = calculate_relative_molecular_mass(formula, True)
    
    if mass is not None:
        print(f'Относительная молекулярная масса формулы {formula} = ~{mass}')
        read_formula(formula)
    else:
        print(f'Ошибка парсинга формулы {formula}')


if __name__ == "__main__":
    main()
