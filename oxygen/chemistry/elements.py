#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химические элементы
 Файл: oxygen/chemistry/elements.py
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
import csv
from typing import Union
from oxygen.base.base import round_to_nearest


class Element:
    def __init__(self, atomic_number: int, name: str, symbol: str, atomic_mass: float,
                neutrons: int, protons: int, electrons: int, period: int, group: int,
                phase: str, radioctive: bool, natural: bool, metall: bool, nonmetall: bool,
                metalloid: bool, element_type: str):
        self.atomic_number = int(atomic_number)
        self.name = name
        self.short_name = symbol
        self.relative_atomic_mass = float(atomic_mass)
        self.neutrons = int(neutrons)
        self.protons = int(protons)
        self.electrons = int(electrons)
        self.period = int(period)
        self.group = group
        self.phase = phase
        if natural == '':
            self.natural = False
        else:
            self.natural = True
        if radioctive == '':
            self.radioctive = False
        else:
            self.radioctive = True
        if metall == '':
            self.metall = False
        else:
            self.metall = True
        if nonmetall == '':
            self.nonmetall = False
        else:
            self.nonmetall = True
        if metalloid == '':
            self.metalloid = False
        else:
            self.metalloid = True
        if element_type == '':
            self.element_type = 'Unknown'
        else:
            self.element_type = element_type


ELEMENTS = []

with open('oxygen/chemistry/data/PeriodicTable.csv', newline='') as File:
    reader = csv.reader(File)
    c = 0
    for row in reader:
        if c == 0:
            c += 1
            continue

        ELEMENTS.append(Element(row[0], row[1], row[2], row[3], row[4], row[5],
                                row[6], row[7], row[8], row[9], row[10],
                                row[11], row[12], row[13], row[14], row[15]))


class MendeleevTable:
    def __init__(self, elements: list) -> None:
        self.elements = elements

    def get_element_by_shortname(self, shortname: str) -> Union[Element, None]:
        for element in self.elements:
            if element.short_name == shortname:
                return element

        return None

    def get_element_by_name(self, name: str) -> Union[Element, None]:
        for element in self.elements:
            if element.name == name:
                return element

        return None

    def get_element_by_number(self, num: int) -> Union[Element, None]:
        for element in self.elements:
            if element.atomic_number == num:
                return element

        return None


MendeleevTable = MendeleevTable(ELEMENTS)
