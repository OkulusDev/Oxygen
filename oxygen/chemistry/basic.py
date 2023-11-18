#!venv/bin/python3
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химия, основы
 Файл: oxygen/chemistry/basic.py
--------------------------------------------------------------------------------
 Описание: Базовые функции для использования химии в ваших проектах
  Пример использования в python-коде
  formula = input("Введите химическую формулу: ")
  result = calculate_relative_molecular_mass(formula)
  print(f"Относительная молекулярная масса для {formula}: {result}")
"""
from mendeleev_table import MendeleevTable


def calculate_relative_molecular_mass(formula):
    stack = []
    current_element = ""
    multiplier = 1

    for char in formula:
        if char.isalpha():
            current_element += char
        elif char.isdigit():
            multiplier = int(char)
        elif char == '(':
            stack.append((current_element, multiplier))
            current_element = ""
            multiplier = 1
        elif char == ')':
            sub_element, sub_multiplier = stack.pop()
            current_element = sub_element + current_element * sub_multiplier

    stack.append((current_element, multiplier))

    total_mass = 0
    for element, multiplier in stack:
        total_mass += atomic_masses[element] * multiplier

    return total_mass
