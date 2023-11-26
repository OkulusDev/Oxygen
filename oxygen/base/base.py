#!/usr/bin/python3
""" Base Functions
Базовые функции

Oxygen
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
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
import math

PI = f'π = {math.pi}'
# AVOGADRO_NUMBER = 6.02 * (10 ** 23)
AVOGADRO_NUMBER = 6.022


def round_to_nearest(num: int):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
