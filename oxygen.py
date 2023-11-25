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

Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
import textwrap
from oxygen.chemistry.base import calculate_relative_molecular_mass, \
                                    calculate_mass_fraction_of_element
from oxygen.chemistry.formulas import read_formula


def get_molecular_mass_from_formule(formula):
    print(f'Расчет формулы {formula}:\n')
    mass = calculate_relative_molecular_mass(formula, True)

    if mass is not None:
        print(f'Относительная молекулярная масса формулы {formula} = ~{mass["mass"]}')
        print(f'Количество протонов в формуле {formula} = ~{mass["protons"]}')
        print(f'Количество электронов в формуле {formula} = ~{mass["electrons"]}')
        print(f'Количество нейтронов в формуле {formula} = ~{mass["neutrons"]}')
    else:
        print(f'Ошибка парсинга формулы {formula}')


def main():
    parser = argparse.ArgumentParser(prog='Oxygen Library', allow_abbrev=True,
                            description='Oxygen',
                            formatter_class=argparse.RawDescriptionHelpFormatter,
						    epilog=textwrap.dedent('''
Примеры использования:

# Включаем режим химии
oxygen.py -c

# Вычисление относительной молекулярной массы формулы
oxygen.py -c -rmm <ФОРМУЛА>

# Вычисление массовой доли элемента в формуле
oxygen.py -c -mf <ФОРМУЛА> -mfe <ЭЛЕМЕНТ ИЗ ФОРМУЛЫ>

# Вычисление относительной молекулярной массы формулы с определением
формулы сложного вещества
oxygen.py -cr -rmm <ФОРМУЛА>

# Вычисление массовой доли элемента в формуле с определением формулы сложного вещества
oxygen.py -cr -mf <ФОРМУЛА> -mfe <ЭЛЕМЕНТ ИЗ ФОРМУЛЫ>

Copyright Okulus Dev (C) 2023
	'''))
    parser.add_argument('-c', '--chemistry-mode', help='включить мод химии',
                        action='store_true')
    parser.add_argument('-r', '--read-formula', help='включить чтение формулы',
                        action='store_true', default=False)
    parser.add_argument('-rmm', '--relative-molecular-mass',
                        help='рассчет молекулярной массы формулы')
    parser.add_argument('-mf', '--mass-fraction', metavar='ФОРМУЛА',
                        help='рассчет массовой доли в формуле')
    parser.add_argument('-mfe', '--mf-element', metavar='ФОРМУЛА',
                        help='элемент для рассчета массовой доли')
    args = parser.parse_args()

    if args.chemistry_mode:
        if args.relative_molecular_mass:
            get_molecular_mass_from_formule(args.relative_molecular_mass)
            if args.read_formula:
                read_formula(args.relative_molecular_mass)
        elif args.mass_fraction:
            if args.mf_element:
                res = calculate_mass_fraction_of_element(args.mass_fraction,
                                                          args.mf_element)
                if args.read_formula:
                    read_formula(args.mass_fraction)
                print(f"Массовая доля {args.mf_element} в \
{args.mass_fraction}: {res}%")
            else:
                print('К сожалению, вы не указали нужный элемент.')
                if args.read_formula:
                    read_formula(args.mass_fraction)


if __name__ == "__main__":
    main()
