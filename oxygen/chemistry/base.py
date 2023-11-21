#!venv/bin/python3
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химия, базовые классы
 Файл: oxygen/chemistry/base.py
--------------------------------------------------------------------------------
 Описание: Базовые функции для использования химии в ваших проектах
  Перечень:
   1. Парсинг элементов из формулы
   2. Вычисление молекулярной массы
   3. Вычисление массовой доли

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
import re
from collections import Counter
from oxygen.chemistry.element import ELEMENTS


def repl(m):
    return m[1] * int(m[2] if m[2] else 1)


def parse_molecule(formula: str) -> dict:
    while '(' in formula:
        formula = re.sub(r'\((\w*)\)(\d*)', repl, formula)
    while '[' in formula:
        formula = re.sub(r'\[(\w*)\](\d*)', repl, formula)
    formula = re.sub(r'([A-Z][a-z]?)(\d*)', repl, formula)
    formula_dict = Counter(re.findall('[A-Z][a-z]*', formula))

    return formula_dict


def get_element_mass(element):
    return ELEMENTS[element].relative_atomic_mass


def calculate_mass_fraction_of_element(formula, element):
    formula = parse_molecule(formula)
    mass_fraction = 0
    mass = 0

    for i in formula.items():
        mass += get_element_mass(i[0]) * i[1]

    for i in formula.items():
        if ELEMENTS[i[0]].short_name == element:
            mass_fraction = (get_element_mass(i[0]) * i[1] / mass) * 100
            break

    return mass_fraction


def calculate_relative_molecular_mass(formula, print_info=False) -> dict:
    result = parse_molecule(formula)
    mass = 0
    neutrons = 0
    electrons = 0
    protons = 0

    for i in result.items():
        try:
            if print_info:
                print(f'{i[1]} {ELEMENTS[i[0]].name} = \
{ELEMENTS[i[0]].relative_atomic_mass * i[1]}')
                print(f'Кол-во протонов в {ELEMENTS[i[0]].short_name} \
({ELEMENTS[i[0]].name}): {ELEMENTS[i[0]].protons}')
                print(f'Кол-во электронов в {ELEMENTS[i[0]].short_name} \
({ELEMENTS[i[0]].name}): {ELEMENTS[i[0]].electrons}')
                print(f'Кол-во нейтронов в {ELEMENTS[i[0]].short_name} \
({ELEMENTS[i[0]].name}): {ELEMENTS[i[0]].neutrons}')

            neutrons += ELEMENTS[i[0]].neutrons
            electrons += ELEMENTS[i[0]].electrons
            protons += ELEMENTS[i[0]].protons

            mass += get_element_mass(i[0]) * i[1]
        except:
            raise ValueError(f'Element {i[0]} does not exists. Try other!')

    return {
        'mass': mass,
        'electrons': electrons,
        'neutrons': neutrons,
        'protons': protons
    }


class ChemicalFormula:
    def __init__(self, elements: dict, formula: str,
                 name: str, molecular_mass: float=None):
        self.elements = elements
        self.formula = formula
        if molecular_mass is not None:
            self.molecular_mass = molecular_mass
        else:
            self.molucular_mass = calculate_relative_molecular_mass(formula, False)
        self.name = name


CHEMICAL_FORMULAS = {
    'H2O': ChemicalFormula({('H', 2), ('O', 1)}, "H2O", 'Вода', None)
}


def read_formula(formula):
    if formula in CHEMICAL_FORMULAS:
        print(f'Формула {formula} это - {CHEMICAL_FORMULAS[formula].name}')
        elements_in_formula = []

        for el in CHEMICAL_FORMULAS[formula].elements:
            elements_in_formula.append(f"{el[1]} {ELEMENTS[el[0]].name}")

        elements_in_formula_str = ", ".join(elements_in_formula)
        print(f'{CHEMICAL_FORMULAS[formula].name} состоит из {elements_in_formula_str}')

