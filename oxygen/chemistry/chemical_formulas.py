"""
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
from oxygen.chemistry.base import calculate_relative_molecular_mass
from oxygen.chemistry.element import MendeleevTable


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
    'H2O': ChemicalFormula({('H', 2), ('O', 1)}, "H2O", 'Вода', None),
    'C12H22O11': ChemicalFormula({('C', 12), ('H', 22), ('O', 11)}, "C12H22O11", 'Сахароза (сахар)', None)
}


def read_formula(formula):
    if formula in CHEMICAL_FORMULAS:
        print(f'Формула {formula} это - {CHEMICAL_FORMULAS[formula].name}')
        elements_in_formula = []

        for el in CHEMICAL_FORMULAS[formula].elements:
            elements_in_formula.append(f"{el[1]} {MendeleevTable.get_element_by_shortname(el[0]).name}")

        elements_in_formula_str = ", ".join(elements_in_formula)
        print(f'{CHEMICAL_FORMULAS[formula].name} состоит из {elements_in_formula_str}')


