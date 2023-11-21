#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Основной файл
 Файл: oxygen/chemistry/elemnent.py
--------------------------------------------------------------------------------
 Описание: файл с химическими элементами

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
from typing import Union
from oxygen.base.base import round_to_nearest


class Element:
    def __init__(self, short_name: str, electronic_conf_of_outer_layer: str,
                name: str, atomic_number: int, relative_atomic_mass: float,
                group: str, period: int, row: int, group_num: int,
                side_group: bool, is_metal: bool) -> None:
        self.short_name = short_name
        self.electronic_conf_of_outer_layer = electronic_conf_of_outer_layer
        self.name = name
        self.atomic_number = atomic_number
        self.relative_atomic_mass = relative_atomic_mass
        self.group = group
        self.side_group = side_group
        self.is_metal = is_metal
        self.period = period
        self.side_group
        self.row = row
        self.group_num = group_num

        self.calculate_protons()
        self.calculate_electrons()
        self.calculate_neutrons()

    def calculate_protons(self) -> float:
        self.protons = self.atomic_number
        return float(self.protons)

    def calculate_electrons(self) -> float:
        self.electrons = self.atomic_number
        return float(self.electrons)

    def calculate_neutrons(self) -> float:
        self.neutrons = round_to_nearest(self.relative_atomic_mass) - self.protons
        return float(self.neutrons)


AVOGADRO_NUMBER = 6.02214076e23

ELEMENTS = {
    # Символ ЭлКонф Название АтомноеЧисло ОтносАтомМасса группа период ряд
    # номерГруппы ЭтопобочнаяГруппа ЭтоМетал
    'H': Element('H', '1s^1', 'Водород', 1, 1.00794, 'A', 1, 1, 1, False, False),
    'He': Element('He', '1s^2', 'Гелий', 2, 4.002602, 'A', 8, 1, 1, False, False),
    'Li': Element('Li', '2s^1', 'Литий', 3, 6.941, 'A', 1, 2, 2, False, True),
    'Be': Element('Be', '2s^2', 'Бериллий', 4, 9.01218, 'A', 2, 2, 2, False, True),
    'B': Element('B', '2s^2 2p^1', 'Бор', 5, 10.811, 'A', 3, 2, 2, False, False),
    'C': Element('C', '2s^2 2p^2', 'Углерод', 6, 12.011, 'A', 4, 2, 2, False, False),
    'N': Element('N', '2s^2 2p^3', 'Азот', 7, 14.0067, 'A', 5, 2, 2, False, False),
    'O': Element('O', '2s^2 2p^4', 'Кислород', 8, 15.9994, 'A', 6, 2, 2, False, False),
    'F': Element('F', '2s^2 2p^5', 'Фтор', 9, 18.998403, 'A', 7, 2, 2, False, False),
    'Ne': Element('Ne', '2s^2 2p^6', 'Неон', 10, 20.179, 'A', 8, 2, 2, False, False),
    'Na': Element('Na', '3s^1', 'Натрий', 11, 22.98977, 'A', 1, 3, 3, False, True),
    'Mg': Element('Na', '3s^2', 'Магний', 12, 24.305, 'A', 2, 3, 3, False, True),
    'Al': Element('Al', '3s^2 3p^1', 'Алюминий', 13, 26.98154, 'A', 3, 3, 3, False, True),
    'Si': Element('Na', '3s^2 3p^2', 'Кремний', 14, 28.0855, 'A', 4, 3, 3, False, False),
    'P': Element('P', '3s^2 3p^3', 'Фосфор', 15, 30.97376, 'A', 5, 3, 3, False, False),
    'S': Element('S', '3s^2 3p^4', 'Сера', 16, 32.066, 'A', 6, 3, 3, False, False),
    'Cl': Element('Cl', '3s^2 3p^5', 'Хлор', 17, 35.453, 'A', 7, 3, 3, False, False),
    'Ar': Element('Ar', '3s^2 3p^5', 'Аргон', 18, 39.948, 'A', 8, 3, 3, False, False),
    "K": Element("K", '4s^1', 'Калий', 19, 39.102, 'A', 1, 4, 4, False, True),
    "Ca": Element('Ca', '4s^2', 'Кальций', 20, 40.08, 'A', 2, 4, 4, False, True),
    'Sc': Element('Sc', '3d^1 4s^2', 'Скандий', 21, 44.956, 'A', 3, 4, 4, False, True),
    'Ti': Element('Ti', '3d^2 4s^2', 'Титан', 22, 47.90, 'B', 4, 4, 4, True, True),
    'V': Element('V', '3d^3 4s^2', 'Ванадий', 23, 50.942, 'B', 5, 4, 4, True, True),
    'Cr': Element('Cr', '3d^5 4s^1', 'Хром', 24, 51.996, 'B', 6, 4, 4, True, True),
    'Mn': Element('Mn', '3d^5 4s^2', 'Марганец', 25, 54.938, 'B', 7, 4, 4, True, True)
}


class MendeleevTable:
    def __init__(self, elements: list) -> None:
        self.elements = elements

    def find_element_by_shortname(self, shortname: str) -> Union[Element, None]:
        for element in self.elements:
            if element.short_name == shortname:
                return element

        return None

