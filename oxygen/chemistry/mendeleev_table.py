#!venv/bin/python3
"""
--------------------------------------------------------------------------------
 Автор: Okulus Dev (aka DrArgentum)
 Лицензия: GNU GPL v3
 Название: Химия, периодическая таблица Менделеева
 Файл: oxygen/chemistry/mendeleev_table.py
--------------------------------------------------------------------------------
 Описание: Базовые функции для использования химии в ваших проектах
  Пример использования в python-коде
  formula = input("Введите химическую формулу: ")
  result = calculate_relative_molecular_mass(formula)
  print(f"Относительная молекулярная масса для {formula}: {result}")
"""


class Element:
    def __init__(self, short_name: str, electronic_conf_of_outer_layer: str, \
                name: str, atomic_number: int, relative_atomic_mass: float, \
                group: str, period: int, row: int, group_num: int, \
                side_group: bool, is_metal: bool):
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

elements = {
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
}

AVOGADRO_NUMBER = 6.02214076e23

