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


def get_molecular_mass_from_formule():
    formula = input('Введите формулу: ')
    print(f'Расчет формулы {formula}:\n')
    mass = calculate_relative_molecular_mass(formula, True)
    
    if mass is not None:
        print(f'Относительная молекулярная масса формулы {formula} = ~{mass["mass"]}')
        print(f'Количество протонов в формуле {formula} = ~{mass["protons"]}')
        print(f'Количество электронов в формуле {formula} = ~{mass["electrons"]}')
        print(f'Количество нейтронов в формуле {formula} = ~{mass["neutrons"]}')
        read_formula(formula)
    else:
        print(f'Ошибка парсинга формулы {formula}')


def main():
    get_molecular_mass_from_formule()


if __name__ == "__main__":
    main()
