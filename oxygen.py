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
from oxygen.chemistry.count_of_substance import count_molecules_from_moles, \
                                                count_moles_from_molecules,
                                                calculate_mass_from_moles


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

# Включить режим химии
oxygen.py -c

# Включить режим вывода информации о формуле, если она есть в базе данных
oxygen.py -r

# Вычисление относительной молекулярной массы формулы
oxygen.py -crmm -f <ФОРМУЛА>

# Вычисление массовой доли элемента в формуле
oxygen.py -c -mf <ФОРМУЛА> -mfe <ЭЛЕМЕНТ ИЗ ФОРМУЛЫ>

# Вычисление количества молекул в формуле 
oxygen.py -cr -N <КОЛИЧЕСТВО ВЕЩЕСТВА>
Например:
oxygen.py -cr -n  2

# Вычисление количества молей в формуле 
oxygen.py -cr -n <КОЛИЧЕСТВО МОЛЕКУЛ>
Например:
oxygen.py -cr -n 24.088

# Вычисление массы в формуле
oxygen.py -cr -m <КОЛИЧЕСТВО МОЛЕЙ> -f <ФОРМУЛА>
Например:
oxygen.py -cr -m 2 -f H2O

Copyright Okulus Dev (C) 2023
	'''))
    parser.add_argument('-c', '--chemistry-mode', help='включить мод химии',
                        action='store_true')
    parser.add_argument('-r', '--read-formula', help='включить чтение формулы',
                        action='store_true', default=False)
    parser.add_argument('-rmm', '--relative-molecular-mass',
                        help='расчет молекулярной массы формулы',)
    parser.add_argument('-mf', '--mass-fraction', metavar='ФОРМУЛА',
                        help='расчет массовой доли в формуле')
    parser.add_argument('-mfe', '--mf-element', metavar='ФОРМУЛА',
                        help='элемент для рассчета массовой доли')
    parser.add_argument('-N', '--count-of-molecules', metavar='КОЛИЧЕСТВО ВЕЩЕСТВА В МОЛЯХ',
                        help='расчет количества молекул')
    parser.add_argument('-n', '--count-of-moles', metavar='КОЛИЧЕСТВО МОЛЕКУЛ',
                        help='расчет количества молей')
    parser.add_argument('-m', '--substance-mass', metavar='КОЛИЧЕСТВО МОЛЕЙ',
                        help='расчет массы вещества')
    parser.add_argument('-f', '--formula', metavar='ФОРМУЛА',
                        help='формула, вспомогательный флаг')
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
        elif args.count_of_molecules:
            if args.count_of_molecules.isdigit():
                result = count_molecules(args.count_of_molecules)
                print(f'N = n * Na = {result} молекул')
                if args.read_formula:
                    read_formula(args.mass_fraction)
            else:
                print('К сожалению, вы ввели не число')
        elif args.count_of_moles:
            result = count_moles(args.count_of_moles)
            print(f'n = N / Na = {result} молей')
            if args.read_formula:
                read_formula(args.mass_fraction)
        elif args.substance_mass:
            if args.formula:
                result = calculate_mass(args.formula, args.substance_mass)
                print(f"m = M * n = {result}")
            else:
                print('Запустите программу с флагом --formula <ФОРМУЛА>')
        else:
            print(args.count_of_molecules)


if __name__ == "__main__":
    main()
