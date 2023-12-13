#!venv/bin/python3
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химия, базовые классы
 Файл: oxygen/chemistry/count_of_substance.py
--------------------------------------------------------------------------------

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
from oxygen.base.base import AVOGADRO_NUMBER as Na
from oxygen.chemistry.base import calculate_relative_molecular_mass


def count_molecules_from_moles(n: int):
    return f"{float(n) * Na} * 10^23"


def count_moles_from_molecules(N: float):
    return float(N) / Na


def calculate_mass_from_moles(formula: str, n: int):
    M = calculate_relative_molecular_mass(formula, False)['mass']
    # return M * float(n)
    return M
