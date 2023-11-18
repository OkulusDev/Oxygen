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
from oxygen.chemistry.mendeleev_table import elements


def calculate_relative_molecular_mass(formula):
    stack = []
    current_element = ""
    multiplier = 1
    prev_el = ""

    for char in formula:
        if char.isalpha():
            if current_element.isalpha():
                # stack.append((current_element, multiplier))
                current_element = char
                multiplier = 1
            else:
                prev_el = char
                current_element += char
        elif char.isdigit():
            if current_element:
                multiplier = int(char)
            else:
                current_element = char
        elif char == '(':
            if current_element:
                if prev_el != current_element:
                    stack.append((f"{prev_el}{current_element}", multiplier))
                else:
                    stack.append((f"{current_element}", multiplier))
                current_element = ""
            stack.append(('(', 1))
            multiplier = 1
        elif char == ')':
            if current_element:
                stack.append((current_element, multiplier))
                current_element = ""
            sub_formula = []
            while stack and stack[-1][0] != '(':
                sub_element, sub_multiplier = stack.pop()
                sub_formula.append(sub_element * sub_multiplier)
            stack.pop()  # Удаляем '(' из стека
            current_element = ''.join(reversed(sub_formula))
            multiplier = 1

    stack.append((current_element, multiplier))
    print(stack)

    total_mass = 0
    for element, multiplier in stack:
        if element == '(':
            print("Ошибка: Неверное использование скобок в формуле.")
            return None
        if element in elements:
            total_mass += elements[element].relative_atomic_mass * multiplier
        else:
            for sub_element in element:
                if sub_element in elements:
                    total_mass += elements[sub_element].relative_atomic_mass * multiplier
                else:
                    print(f"Ошибка: Неизвестный элемент {sub_element} в формуле.")
                    return None

    return total_mass
