# Oxygen
Программное обеспечение для инженерных вычислений, научно-естественных наук, математики и алгоритмов

![Static Badge](https://img.shields.io/badge/OkulusDev-Oxygen-Oxygen)
![GitHub top language](https://img.shields.io/github/languages/top/OkulusDev/Oxygen)
![GitHub](https://img.shields.io/github/license/OkulusDev/Oxygen)
![GitHub Repo stars](https://img.shields.io/github/stars/OkulusDev/Oxygen)
![GitHub issues](https://img.shields.io/github/issues/OkulusDev/Oxygen)

## Установка (Linux)
У вас должен быть установлены [зависимости проекта](https://github.com/OkulusDev/Oxygen#зависимости)

1. Клонирование репозитория 

```git clone https://github.com/OkulusDev/Oxygen.git```

2. Переход в директорию Oxygen

```cd Oxygen```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта для демонстрации возможностей Oxygen

```python3 oxygen.py --help```

## Документация
Пользовательскую документацию можно получить по [этой ссылке](./docs/ru/index.md).

[Релизы программы]: https://github.com/OkulusDev/Oxygen/releases

## Поддержка
Если у вас возникли сложности или вопросы по использованию пакета, создайте 
[обсуждение](https://github.com/OkulusDev/Oxygen/issues/new/choose) в данном репозитории или напишите на электронную почту <bro.alexeev@gmail.com>.

## Зависимости
Эта программа зависит от интепретатора Python версии 3.7 или выше, PIP 23.2.1 или выше. Если вы заметили, что он данное ПО можно запустить на версии ниже, или он не работает на какой-либо версии, то напишите в [поддержку](https://github.com/OkulusDev/Oxygen#поддержка)

## Описание коммитов
| Название | Описание                                                        |
|----------|-----------------------------------------------------------------|
| build	   | Сборка проекта или изменения внешних зависимостей               |
| ci       | Настройка CI и работа со скриптами                              |
| docs	   | Обновление документации                                         |
| feat	   | Добавление нового функционала                                   |
| fix	   | Исправление ошибок                                              |
| perf	   | Изменения направленные на улучшение производительности          |
| refactor | Правки кода без исправления ошибок или добавления новых функций |
| revert   | Откат на предыдущие коммиты                                     |
| style	   | Правки по кодстайлу (табы, отступы, точки, запятые и т.д.)      |
| test	   | Добавление тестов                                               |
