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


class Element:
    def __init__(self, short_name: str, electronic_conf_of_outer_layer: str, \
                name: str, atomic_number: int, relative_atomic_mass: float):
        self.short_name = short_name
        self.electronic_conf_of_outer_layer = electronic_conf_of_outer_layer
        self.name = name
        self.atomic_number = atomic_number
        self.relative_atomic_mass = relative_atomic_mass


