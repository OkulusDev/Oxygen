#!venv/bin/python3
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химия, базовые классы
 Файл: oxygen/chemistry/base.py
--------------------------------------------------------------------------------
 Описание: Базовые функции для использования химии в ваших проектах
  Пример использования в python-коде
  formula = input("Введите химическую формулу: ")
  result = calculate_relative_molecular_mass(formula)
  print(f"Относительная молекулярная масса для {formula}: {result}")
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


def calculate_relative_molecular_mass(formula, print_info=False):
    result = parse_molecule(formula)
    mass = 0

    for i in result.items():
        if print_info:
            print(f'{i[1]} {ELEMENTS[i[0]].name} = {ELEMENTS[i[0]].relative_atomic_mass * i[1]}')

        mass += get_element_mass(i[0]) * i[1]

    return mass


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
