# Эволюционно-генетический алгоритм для задачи о рюкзаке

## Цель проекта
Реализовать решение задачи о рюкзаке с помощью генетического алгоритма. Логика построена по модульному принципу, ведётся логирование результатов в Excel.

## Стек технологий
Python, Pandas, openpyxl, random, math, os, typing

## Этапы работы
- Формализация задачи
- Реализация скрещивания, мутаций и селекции
- Ведение логов в Excel
- Настройка параметров и визуальный контроль

## Результат
Найдено приближённое решение задачи, построенная архитектура легко адаптируется под другие задачи оптимизации.

## Пример параметров задачи

```python
items = [
    {'weight': 4, 'value': 10},
    {'weight': 2, 'value': 7},
    {'weight': 5, 'value': 13},
    # ...
]
MAX_WEIGHT = 15
POPULATION_SIZE = 30
NUM_GENERATIONS = 50
```

Каждое решение — бинарный вектор длины N, где `1` — предмет включён в рюкзак, `0` — нет.

## Структура проекта

```
EGA_DATA_RECORDING/
├── main.py
├── data.py
├── data_recording.py
├── complete_bust/
│   ├── complete_bust.py
│   └── full_list.py
├── crossover/
│   ├── choosing_crossover.py
│   └── crossover_operators.py
├── initial_population/
│   ├── choosing_init_popul.py
│   └── methods_creating_initial_population.py
├── mutation/
│   ├── choosing_mutation.py
│   └── mutation_operators.py
├── parent_couple/
│   └── methods_pair_selection.py
├── processing_restrictions/
│   └── ways_restrictions_processing.py
├── selection/
│   └── selection_operators.py
├── *.xlsx (результаты по поколениям)
```

## Контакты

* Telegram: \[[https://t.me/Xobortz](https://t.me/Xobortz)]
* Email: \[[genaj.2000@yandex.ru](mailto:genaj.2000@yandex.ru)]
* Профиль: [https://github.com/XOBORT](https://github.com/XOBORT)
